##############################################################################################
def function_handler(event, context):
    event["response"] = {"autoConfirmUser": True}
    return event
