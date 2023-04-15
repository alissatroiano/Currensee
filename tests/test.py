import argparse
import json
import mindsdb

"""
Checks the status of a model (generating, training, error, or complete).
Example usage: python ./scripts/getStatus.py --name btcusdt_model
"""

# Initialize argument parser
parser = argparse.ArgumentParser(description='Check the status of a MindsDB model')
parser.add_argument('-c', '--config-path', default='./config/mindsdb-config.json',
                    help='path to config JSON file used for connecting to MindsDB.')
parser.add_argument('-n', '--name', default='./config/model-config.json',
                    help='name of the model to check the status for')
args = parser.parse_args()

# Load MindsDB configuration from JSON file
with open(args.config_path) as f:
    config = json.load(f)

async def main():
    mdb = mindsdb.Predictors(**config)
    await mdb.connect()
    return await mdb.get_model(model_name=args.name)

# Check model status
async def check_model_status():
    try:
        model = await main()
        if model:
            print(f"Status of model {model.name} is {model.status}")
        else:
            print(f"Model with name {args.name} does not exist")
    except Exception as e:
        print(f"Fetching model failed with error: {e}")

# Run the program
if __name__ == '__main__':
    check_model_status()
