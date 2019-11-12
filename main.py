import facebook

page_id = "114266900019151"  # Random Philippine Law Bot Page ID
access_token = "EAAKcR3BGoK8BAGkfcb4AYfdZA7EHNBGhDCg0U8NAxlZArFvCNFyRZCFKDdy42zY5VxBZAWJ1ZBC5rkPeoYQl51zZBucfnwSRgvkhmc3bFPqtFWQztmmYZB3t3FDyTAajC7nO8FNf9QZAeAlmhEHRBFTZCpP0m7C2ebin2mFZAls8KpCiLc60B9tF7MgSV2a9yYLZBc6vxGIfejTNgZDZD"
message = "Another Test"
graph = facebook.GraphAPI(access_token)

graph.put_object(parent_object=page_id, connection_name="feed", message=message) #Posts the Message post
