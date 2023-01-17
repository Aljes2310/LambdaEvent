# **Tarea U6 Silabuz**

## _Funcion Lambda_
## **Alumno**: Alfredo Alvarado Espinoza
## **Aula**: A3


La siguiente funcion esta diseñada para recibir eventos en las cuales se realize un pago.


En la funcion onsubmit del proyecto en react de mercadopago, se cambia el endpoint dirigiendo a la API Gateway de AWS lambda y se añade el parametro de "no-cors" en el fetch. 

```javascript
onSubmit: async (cardFormData: any) => {
            const response = await fetch(
              "https://bxqtqnuuc5.execute-api.us-east-2.amazonaws.com/default/lambdaEvaluacion",
              {
                method: "POST",
                headers: {
                  "Content-Type": "application/json", 
                }, mode: 'no-cors',
                body: JSON.stringify(cardFormData),
              }
            );
            console.log("response", response);
          },
```


