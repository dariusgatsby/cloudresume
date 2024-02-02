import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'Visitors'
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    visitor_id = 'unique_visitor_id'
    response= table.update_item(
    Key={
        'visitor_id': visitor_id,
    },
    UpdateExpression='SET visit_count = visit_count + :val1',
    ExpressionAttributeValues={
        ':val1': 1
    }
)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Visit count updated successfully'}),
        'headers': {
            'Content-Type': 'application/json',
        },
}