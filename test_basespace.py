from Basespace import create_project, get_datasets


def test_create_project():
    create_project("My Project")
    
    
def test_get_datasets():
    import os
    project_id = os.environ.get( "PROJECT_ID" )
    topic_name = os.environ.get( "TOPIC_NAME" )
    datasets = get_datasets( project_id, topic_name )
    print(datasets)



