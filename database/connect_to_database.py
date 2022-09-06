from google.cloud import bigquery
import pandas

class ConnectToDataBase():
    def __init__(self):
        pass
    @staticmethod    
    def insert_rows(dataset,
                    table,
                    rows_to_insert):
        client = bigquery.Client()
        table_ref = client.dataset(dataset).table(table)
        table = client.get_table(table_ref)
        errors = client.insert_rows(table,
                                    rows_to_insert)
        
        return errors
    
    @staticmethod            
    def get_values(query):
        return pandas.read_gbq(query)
 

    @staticmethod    
    def run_query(query = None,
                  parameters = None,
                    values = None):
        client = bigquery.Client()
        query_parameters =[]
        count = 0
        for key in parameters.keys():
            query_parameters.append( bigquery.ScalarQueryParameter(key,
                                                                    parameters[key],
                                                                      values[count]))
            count = count + 1
                                     
        job_config = bigquery.QueryJobConfig(query_parameters = query_parameters)
        query_job = client.query(query,
                                 job_config = job_config)
        return query_job.result()
    
    

class JobConfig():
    def __init__(self):
        pass
    def create_parameters(self,parameters,
                          list_values):
        query_parameters = []
        k=0
        for value in list_values:
            if value is not None:
                query_parameters.append(bigquery.ScalarQueryParameter(parameters[0][k],
                                                                      parameters[1][k],
                                                                      value)
                                       )
            k=k+1
        return query_parameters