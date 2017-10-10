from es_client_factory import ESClientFactory


class EsDAO:
    @classmethod
    def fetch_data(cls, index, document_type, query):
        es = ESClientFactory.es_client_instance()
        return es.search(index=cls.index,
                         doc_type=cls.document_type,
                         body=query, request_timeout=120)


