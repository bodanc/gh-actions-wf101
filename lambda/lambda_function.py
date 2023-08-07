from github import Github


def lambda_handler(event, context):
    """Wrapper for a very basic lambda function
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n---------------------------------------------'

    if event["input"] == "Hello":
        return "World"
    else:
        raise
