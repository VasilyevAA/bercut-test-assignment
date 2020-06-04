


def test_positive_additional(additional_request):
    code, data = additional_request({'arg1': '111', 'arg2': '231.12'})

def test_positive_additional_very_big_numbers(test_client):
    data = test_client.post("/v1/add", json={'arg1': '1234567890', 'arg2': '231.12'})
    print('keks')
