import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    data = json.loads(event["body"])
    
    #siguiendo el ejemplo de webhook de la pagina de mercadopago
    payment_data = {
    "transaction_amount": float(data["transaction_amount"]),
    "token": data["token"],
    "installments": int(data["installments"]),
    "payment_method_id": data["payment_method_id"],
    "payer": {
        "email": data["payer"]["email"],
        "identification": {
            "type": data["payer"]["identification"]["type"], 
            "number": data["payer"]["identification"]["number"]
            }
         }
    }

    payment_response = sdk.payment().create(payment_data)
    preference_response = payment_response["response"]

    return { "statusCode": 200, 
        "body": json.dumps(preference_response),}
