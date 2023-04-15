from flask import Flask, jsonify, request
import json
import mindsdb

app = Flask(__name__)

@app.route('/check_model_status', methods=['GET'])
def check_model_status_route():
    # Get model name from query parameter
    model_name = request.args.get('crypto4')
    
    # Load MindsDB configuration from JSON file
    with open('./config/mindsdb-config.json') as f:
        config = json.load(f)

    async def main():
        mdb = mindsdb.Predictors(**config)
        await mdb.connect()
        return await mdb.get_model(model_name=model_name)

    # Check model status
    async def check_model_status():
        try:
            model = await main()
            if model:
                return {'status': f"Status of model {model.name} is {model.status}"}
            else:
                return {'error': f"Model with name {model_name} does not exist"}
        except Exception as e:
            return {'error': f"Fetching model failed with error: {e}"}

    # Run the program
    result = check_model_status()
    # return jsonify(result)
    print(result)
