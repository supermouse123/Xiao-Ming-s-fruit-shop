from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client

class FDFSStorage(Storage):
    """fast fds文件存储类"""

    def __init__(self, client_conf=None, base_url=None):
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        """打开文件时候使用"""
        pass

    def _save(self, name, content):
        """保存文件时候用"""
        #name:选择上传文件的名字
        #content:包含上传文件内容对象
        client = Fdfs_client('./utils/fdfs/client.conf')
        res = client.upload_by_buffer(content.read())

        if res.get('Status') != 'Upload successed.':
            raise Exception('上传文件到fast dfs 失败')

        filename = res.get('Remote file_id')
        return filename

    def exists(self, name):
        """Dajngo判断文件名是否有用"""
        return False

    def url(self, name):
        return self.base_url + name