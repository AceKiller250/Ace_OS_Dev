from mega import Mega

mega = Mega()


m = mega.login("peytonanthony99@gmail.com", "fInrif-nywpo4-darwuj")
# login using a temporary anonymous account


file = m.upload('calcv3.py')
print(m.get_upload_link(file))

file = m.find('AceOS', exclude_deleted=True)
m.download(file)