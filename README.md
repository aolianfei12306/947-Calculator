# 947-Calculator / 947计算器

一个基于 Streamlit 的在线计算器，支持本地部署和 ngrok 公网访问。

A Streamlit-based online calculator that supports local deployment and public access via ngrok.

## 功能特性 / Features

- 🧮 **基础计算** / Basic Calculator
  - 加法、减法、乘法、除法
  - Addition, Subtraction, Multiplication, Division

- 🔬 **科学计算** / Scientific Calculator
  - 平方根、平方、立方
  - Square Root, Square, Cube
  - 对数函数（自然对数、常用对数、二进制对数）
  - Logarithmic Functions (Natural, Common, Binary)
  - 指数函数
  - Exponential Functions
  - 三角函数（sin, cos, tan）
  - Trigonometric Functions (sin, cos, tan)

- 📝 **计算历史** / Calculation History
  - 自动保存最近的计算记录
  - Automatically saves recent calculations

- 🌐 **部署方式** / Deployment Options
  - 本地部署
  - Local Deployment
  - Ngrok 公网访问
  - Public Access via Ngrok

## 安装 / Installation

### 1. 克隆仓库 / Clone Repository

```bash
git clone https://github.com/aolianfei12306/947-Calculator.git
cd 947-Calculator
```

### 2. 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

## 使用方法 / Usage

### 方式一：本地部署 / Method 1: Local Deployment

#### 使用 Streamlit 直接运行 / Run directly with Streamlit:

```bash
streamlit run app.py
```

然后在浏览器中打开 http://localhost:8501

Then open http://localhost:8501 in your browser

#### 使用运行脚本 / Using the run script:

```bash
python run.py
```

### 方式二：使用 Ngrok 公网访问 / Method 2: Public Access with Ngrok

#### 前提条件 / Prerequisites:

1. 在 [ngrok 官网](https://ngrok.com/) 注册账号
2. 获取你的 authtoken: https://dashboard.ngrok.com/get-started/your-authtoken
3. 配置 ngrok token（选择以下任一方式）:

Register at [ngrok website](https://ngrok.com/)
Get your authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken
Configure ngrok token (choose one method):

**方法 A / Method A**: 使用 ngrok CLI 配置 / Configure via ngrok CLI

```bash
ngrok config add-authtoken YOUR_TOKEN
```

**方法 B / Method B**: 通过命令行参数传递 / Pass via command line

```bash
python run.py --ngrok --token YOUR_TOKEN
```

#### 启动服务 / Start the service:

```bash
python run.py --ngrok
```

运行后，你将看到：
After running, you will see:

```
============================================================
✅ 947 Calculator is now running!
============================================================
📍 Local URL:  http://localhost:8501
🌐 Public URL: https://xxxx-xx-xx-xx-xx.ngrok.io
============================================================
```

使用 Public URL 即可从任何地方访问你的计算器！

Use the Public URL to access your calculator from anywhere!

## 项目结构 / Project Structure

```
947-Calculator/
├── app.py              # 主应用程序 / Main application
├── run.py              # 运行脚本 / Run script
├── requirements.txt    # 依赖列表 / Dependencies
├── .env.example        # 环境变量示例 / Environment variables example
└── README.md           # 项目文档 / Project documentation
```

## 技术栈 / Tech Stack

- **Streamlit**: Web 应用框架 / Web application framework
- **Python**: 编程语言 / Programming language
- **Ngrok**: 内网穿透工具 / Tunneling tool for public access

## 常见问题 / FAQ

### Q: 如何停止服务？ / How to stop the service?

A: 在终端按 `Ctrl+C` / Press `Ctrl+C` in terminal

### Q: Ngrok 连接失败？ / Ngrok connection failed?

A: 检查以下内容 / Check the following:
1. 确保已安装 pyngrok: `pip install pyngrok`
2. 确保 ngrok token 配置正确
3. 检查网络连接

### Q: 如何修改端口？ / How to change port?

A: 修改 `run.py` 中的 `port` 变量，或使用 streamlit 参数：
   Modify the `port` variable in `run.py`, or use streamlit parameters:

```bash
streamlit run app.py --server.port 8502
```

## 贡献 / Contributing

欢迎提交 Issue 和 Pull Request！

Issues and Pull Requests are welcome!

## 许可证 / License

MIT License
