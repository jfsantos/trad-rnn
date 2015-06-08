import requests

base_url = "http://thesession.org/tunes/%d/abc"
n_files = 14010

for k in range(1, n_files):
    if k % 100 == 0:
        print "Downloading file %d/%d" % (k, n_files)
    try:
        r = requests.get(base_url % k)
        if r.status_code == 200:
            f = open("abc/%d.abc" % k, "w")
            f.write(r.text.encode("UTF-8"))
    except Exception as ex:
        print ex


