from Cloud.packages.sns import sns_manager


##############################################################################################


def function_handler(event, context):
    # send to sns event to delete all items with C# (faster)
    topic_arn = sns_manager.get_topic_by_name("DropBlocksTable")[0]["TopicArn"]
    sns_manager.sns_publish_to_topic(topic_arn=topic_arn, message="delete all blocks", subject="delete all blocks")

##############################################################################################
