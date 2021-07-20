# 引入APP配置
from app.factory import create_app

app = create_app("config")

# 程序执行入口
if __name__ == "__main__":
    app.run(port=5000, debug=True)
