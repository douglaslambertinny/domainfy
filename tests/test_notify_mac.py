from domainfy import notify


def test_notify_message():
    assert notify('Title', 'Heres an alert') is True


def test_notify_message_with_special_characters():
    assert notify(r'Weird\/|"!@#$%^&*()\ntitle', r'!@#$%^&*()"') is True
