from elasticsearch import Elasticsearch

class ESClientFactory:
    _es_client = None
    #_conf_service = ConfigurationService()

    @classmethod
    def es_client_instance(cls):
        if cls._es_client is None:
            cls._es_client = cls._create_client()
        return cls._es_client

    # @classmethod
    # def _create_client(cls):
    #     if None not in [cls._conf_service.lambda_aws_access_key,
    #                     cls._conf_service.lambda_aws_secret_access_key,
    #                     cls._conf_service.aws_session_token]:
    #         print('creating secure es client...')
    #         auth = AWSRequestsAuth(aws_access_key = cls._conf_service.lambda_aws_access_key,
    #                                aws_secret_access_key = cls._conf_service.lambda_aws_secret_access_key,
    #                                aws_token = cls._conf_service.aws_session_token,
    #                                aws_host = cls._conf_service.elastic_search_host,
    #                                aws_region = cls._conf_service.aws_default_region,
    #                                aws_service = 'es')
    #         return Elasticsearch([cls._conf_service.elastic_search_url],
    #                                port=443,
    #                                connection_class=RequestsHttpConnection,
    #                                http_auth=auth)
    #     else:
    #         print('creating es client...')
    #         return Elasticsearch([cls._conf_service.elastic_search_url],
    #                              port=443)

    @classmethod
    def _create_client(cls):
        return Elasticsearch(
            ['https://search-elasticsearch-prod00-uaiyztdprcfqlukwr3xiequjzm.us-east-1.es.amazonaws.com'],
            port=443)

