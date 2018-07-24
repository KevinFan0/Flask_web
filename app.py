from flask import Flask, jsonify, request, render_template
from werkzeug.wrappers import Response
from flask.views import View

app = Flask(__name__, template_folder='')

#响应
class JSONResponse(Response):
    @classmethod
    def force_type(cls,rv,environ=None):
        if isinstance(rv,dict):
            rv = jsonify(rv)
        return super(JSONResponse,cls).force_type(rv,environ)

app.response_class = JSONResponse

@app.route('/')
def hello_world():
    return {'message':'Hello,World!'}

@app.route('/custom_headers')
def headers():
    return {'headers':[1,2,3]},201,[('X-Request-Id','100')]

#标准视图
class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self,context):
        return render_template(self.get_template_name, **context)

    def dispatch_request(self):
        if request.method != 'GET':
            return "UNSUPPORTED"
        context = {'users':self.get_users()}
        return self.render_template(context)

class UserView(BaseView):
    def get_template_name(self):
        return 'chapter3/section1/users.html'

    def get_users(self):
        return [{
            'username':'fake',
            'avatar':'http://lorempixel.com/100/100/nature'
        }]

app.add_url_rule('/users',view_func=UserView.as_view('userview'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
