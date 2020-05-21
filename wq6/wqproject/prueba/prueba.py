import boto3
import json

cliente = boto3.client('lambda')

payload = { 'x': '1017', }
payload = json.dumps(payload)

'''
response = cliente.invoke(
    FunctionName='my-function',
    Payload=payload,
    Qualifier='3',
)
print (response['Payload'].read().decode("utf-8"))
'''

response = cliente.list_functions()

print (response)
