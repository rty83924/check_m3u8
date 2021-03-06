import yaml
import os
a = os.path.dirname(os.path.abspath(__file__))
# Loader=yaml.FullLoader 取消yml.load 不安全僅告
class sendurl:
    def __init__(self):
        pass
        stream_name = list()
        domain_name = list()
        stream_app = list()
        self.stream_name = stream_name
        self.domain_name = domain_name
        self.stream_app = stream_app
    def domain(self):
        with open('{}/config/domain.yml'.format(a), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        data = data['domain']
        data = list(data)
        self.domain_name = data
        return self.domain_name
    def streamName(self):
        with open('{}/config/app.yml'.format(a), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        data = data['app']
        data = list(data)
        self.stream_name = data
        return self.stream_name
    def streamApp(self):
        with open('{}/config/stream.yml'.format(a), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        data = data['stream']
        data = list(data)
        self.stream_app = data
        #print(self.stream_app)
        return self.stream_app


class saveurl:
    #sendurl = sendurl(self)
    def __init__(self):
        pass
    def tryurl(self):
        urllist= list()
        domain = sendurl().domain()
        streamApp = sendurl().streamApp()
        streamName = sendurl().streamName()
        for i in domain:
            for y in streamApp:
                for j in streamName:
                    urllist.append('https://{}/{}/{}'.format(i, y, j))
        return urllist

if __name__ == '__main__':
#    sendurl = sendurl()
#   print(sendurl.domain())
#    print(sendurl.streamApp())
    saveurl = saveurl()
    print(saveurl.tryurl())