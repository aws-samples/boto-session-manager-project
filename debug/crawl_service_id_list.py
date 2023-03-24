# -*- coding: utf-8 -*-

"""
Crawl `boto3 documentation site <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html>`_,
find all client id and automatically generate code for this library.
"""

import typing as T

import re
import json
import dataclasses
from functools import cached_property

import jinja2
import requests
from jinja2 import Template
from bs4 import BeautifulSoup
from diskcache import Cache
from pathlib_mate import Path


# ------------------------------------------------------------------------------
dir_here = Path.dir_here(__file__)
dir_project_root = dir_here.parent
dir_cache = Path(dir_here, ".cache")

cache = Cache(dir_cache.abspath)
cache_expire = 24 * 3600  # expires in 1 day

path_spec_file_json = Path(dir_here, "spec-file.json")
path_services_py = Path(dir_project_root, "boto_session_manager", "services.py")
path_clients_py = Path(dir_project_root, "boto_session_manager", "clients.py")
path_services_template = Path(dir_here, "services.jinja2")
path_clients_template = Path(dir_here, "clients.jinja2")
# ------------------------------------------------------------------------------


def get_html_with_cache(url: str) -> str:
    """
    Crawl the URL HTML content, store it to the disk cache.

    :param url: webpage URL
    :return: HTML
    """
    if url in cache:
        return cache.get(url)
    else:
        html = requests.get(url).text
        cache.set(url, html, expire=cache_expire)
        return html


@dataclasses.dataclass
class AWSService:
    """
    ServiceHomepage Dataclass

    :param name: it is the clickable text in the boto3 document homepage sidebar.
        For example, for Elastic Block Storage service, the url is
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html,
        the clickable text in the sidebar is "EBS".
    :param href_name: the last part of the document url.
        For example, for Elastic Block Storage service, the url is
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html,
        the last part is "ebs".
    :param doc_url: the boto3 document url
    :param service_id: the service id that can be used in boto3.client("${service_id}")
    """

    name: str = dataclasses.field()
    href_name: str = dataclasses.field()
    doc_url: str = dataclasses.field()
    service_id: str = dataclasses.field()

    @property
    def name_snake_case(self) -> str:
        return self.name.lower().replace("-", "_")

    @property
    def service_id_snake_case(self) -> str:
        return self.service_id.lower().replace("-", "_")

    @property
    def service_id_camel_case(self) -> str:
        return "".join([
            word[0].upper() + word[1:]
            for word in self.name.lower().split("-")
        ])


def crawl_service_page(html: str) -> str:
    """
    Given an AWS Service boto3 API documentation webpage HTML,

    extract the string token that used to create boto3 client.

    For example, given EBS boto3 API doc at https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html
    it returns "ebs", so we can use boto3.client("ebs") to create ebs client.

    :param html:

    :return: service id
    """
    pattern = re.compile("client = boto3.client\('[\d\D]*'\)")
    soup = BeautifulSoup(html, "html.parser")
    div_client = soup.find("div", class_="highlight-default notranslate")
    service_id = None
    for line in div_client.text.split("\n"):
        res = re.findall(pattern, line)
        if len(res):
            service_id = res[0].split("'")[1]
    return service_id


def crawl_home_page(html: str):
    """
    get all AWS Service boto3 api homepage from the boto3 doc homepage,
    from its sidebar.
    """
    aws_service_list = list()
    soup = BeautifulSoup(html, "html.parser")
    ul = soup.find("ul", class_="current")
    for a in ul.find_all("a", class_="reference internal"):
        # make sure the link is an aws service link
        if "#" not in a.attrs["href"]:
            href_name = a.attrs["href"]
            name = a.text
            doc_url = f"https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/{href_name}"
            aws_service = AWSService(
                name=name,
                href_name=href_name,
                doc_url=doc_url,
                service_id="",
            )
            # print(aws_service)
            aws_service_list.append(aws_service)
    return aws_service_list


def get_all_aws_service() -> T.List[AWSService]:
    """
    get all AWS Service boto3 api homepage from the boto3 doc homepage,
    from its sidebar.
    """
    url_available_services = "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html"
    html = get_html_with_cache(url_available_services)
    aws_service_list = crawl_home_page(html)
    return aws_service_list


def step1_crawl_spec_file_data():
    # --------------------------------------------------------------------------
    # get all AWS Service boto3 api homepage from the boto3 doc homepage,
    # from its sidebar.
    # --------------------------------------------------------------------------
    print("get all AWS service ...")
    url_available_services = "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html"
    html = get_html_with_cache(url_available_services)
    aws_service_list = crawl_home_page(html)
    print(f"found {len(aws_service_list)} AWS Services that has boto3 API")


    # --------------------------------------------------------------------------
    # iterate through all service page, and extract service_id
    # --------------------------------------------------------------------------
    print("extract service_id ...")
    for aws_service in aws_service_list:
        print(f"working on {aws_service.doc_url} ...")
        html = get_html_with_cache(aws_service.doc_url)
        service__id = crawl_service_page(html)
        aws_service.service_id = service__id

    # --------------------------------------------------------------------------
    # dump service data
    # --------------------------------------------------------------------------
    print("dump service data ...")
    spec_file_data: T.List[T.Dict[str, str]] = [
        dataclasses.asdict(aws_service)
        for aws_service in aws_service_list
    ]
    path_spec_file_json.write_text(json.dumps(spec_file_data, indent=4))


# import mypy_boto3_s3
# python -m pip install 'boto3-stubs-lite[essential]'`
import boto3

s3_client = boto3.session.Session().client("s3")


def step2_generate_code():
    spec_file_data = json.loads(path_spec_file_json.read_text())

    # Generate services.py and clients.py
    services_py_lines = [
        "# -*- coding: utf-8 -*-",
        "",
        "",
        "class AwsServiceEnum:",
    ]
    clients_py_lines = [
        "# -*- coding: utf-8 -*-",
        "",
        "import typing as T",
        "",
        "from .services import AwsServiceEnum",
        "",
        "if T.TYPE_CHECKING:",
        "    from .manager import BotoSesManager",
        "",
        "class ClientMixin:",
    ]

    aws_service_list = [
        AWSService(**dct)
        for dct in spec_file_data
    ]

        # Generate clients.py
        # clients_py_lines.extend(
        #     [
        #         f"    @property",
        #         f'    def {name_snake_case}_client(self: "BotoSesManager"):',
        #         f'        """',
        #         f"        Ref: {doc_url}",
        #         f'        """',
        #         f"        return self.get_client(AwsServiceEnum.{name})",
        #         f"",
        #     ]
        # )
    # services_py_lines.append("")

    path_services_py.write_text(
        jinja2.Template(path_services_template.read_text()).render(
            aws_service_list=aws_service_list,
        )
    )
    path_clients_py.write_text(
        jinja2.Template(path_clients_template.read_text()).render(
            aws_service_list=aws_service_list,
        )
    )
    # path_clients_py.write_text("\n".join(clients_py_lines))


# step1_crawl_spec_file_data()
step2_generate_code()
