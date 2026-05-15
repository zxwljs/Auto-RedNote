# 小红书笔记创作技能 (xhs-note-creator)

一个专业的小红书笔记素材创作工具，支持内容撰写、图片卡片生成和笔记发布。

## 📁 项目结构

```
xhs-note-creator/
├── assets/                   # 资源文件
│   ├── themes/              # 8种排版主题
│   │   ├── default.css
│   │   ├── playful-geometric.css
│   │   ├── neo-brutalism.css
│   │   ├── botanical.css
│   │   ├── professional.css
│   │   ├── retro.css
│   │   ├── sketch.css
│   │   └── terminal.css
│   ├── card.html            # 正文卡片模板
│   ├── cover.html           # 封面模板
│   ├── styles.css           # 共用样式
│   └── example.md           # 示例文档
├── scripts/                 # 脚本文件
│   ├── render_xhs.py        # 图片渲染脚本
│   └── publish_xhs.py       # 小红书发布脚本
├── SKILL.md                 # 技能详细文档
├── requirements.txt         # Python依赖
└── .env                     # 环境配置文件
```

## 🚀 快速开始

### 1. 安装依赖

```bash
# 安装Python依赖
pip install -r requirements.txt

# 安装Playwright浏览器
playwright install
```

## 📝 使用方法

### 第一步：创建Markdown内容

创建包含YAML头部的Markdown文件：

```markdown
---
emoji: "🚀"
title: "5个效率神器让工作效率翻倍"
subtitle: "对着抄作业就好了，一起变高效"
---

# 📝 神器一：Notion

> 全能型笔记工具，支持数据库、看板、日历等多种视图...

## 特色功能
- 特色一
- 特色二
```

### 第二步：渲染图片卡片

```bash
# 基本用法
python scripts/render_xhs.py content.md

# 指定输出目录和主题
python scripts/render_xhs.py content.md -o ./output -t playful-geometric

# 自动切分分页（推荐）
python scripts/render_xhs.py content.md -m auto-split

# 动态高度模式
python scripts/render_xhs.py content.md -m dynamic --max-height 4320
```

### 第三步：发布小红书笔记（可选）

```bash
python scripts/publish_xhs.py \
  --title "笔记标题" \
  --desc "笔记描述内容" \
  --images cover.png card_1.png card_2.png
```

## 🎨 主题选择

| 主题名称 | 风格特点 |
|---------|---------|
| `default` | 默认简约浅灰渐变 |
| `playful-geometric` | 活泼几何（Memphis设计） |
| `neo-brutalism` | 新粗野主义（粗边框、高饱和） |
| `botanical` | 植物园自然（森林绿） |
| `professional` | 专业商务风格 |
| `retro` | 复古怀旧风格 |
| `terminal` | 终端命令行风格 |
| `sketch` | 手绘素描风格 |

## 📐 分页模式

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| `separator` | 按 `---` 分隔符分页 | 内容已手动控量 |
| `auto-fit` | 固定尺寸自动缩放文字 | 封面+单张图片 |
| `auto-split` | 按高度自动切分 | 长文内容（推荐） |
| `dynamic` | 动态调整高度 | 内容长短不一 |

## 📊 图片规格

| 类型 | 尺寸 | 比例 |
|------|------|------|
| 封面卡片 | 1080×1440px | 3:4 |
| 正文卡片 | 1080×1440px | 3:4 |

## ⚙️ 渲染参数

```bash
python scripts/render_xhs.py <markdown_file> [options]

选项:
  -o, --output-dir    输出目录（默认：当前目录）
  -t, --theme         排版主题（默认：default）
  -m, --mode          分页模式（默认：separator）
  -w, --width         图片宽度（默认：1080）
  --height            图片高度（默认：1440）
  --max-height        dynamic模式最大高度（默认：4320）
  --dpr               设备像素比（默认：2）
```

## 📖 完整工作流示例

```bash
# 1. 创建内容文件
cat > content.md << 'EOF'
---
emoji: "💡"
title: "高效工作技巧分享"
subtitle: "提升效率的5个秘诀"
---

# 🔹 技巧一：番茄工作法

25分钟专注 + 5分钟休息，保持高效状态。

---

# 🔹 技巧二：任务优先级

使用四象限法则管理任务优先级。

#高效工作 #时间管理 #效率提升
EOF

# 2. 渲染图片（使用活泼几何主题）
python scripts/render_xhs.py content.md -t playful-geometric -m auto-split

# 3. 发布到小红书
python scripts/publish_xhs.py \
  --title "高效工作技巧分享" \
  --desc "分享5个提升工作效率的实用技巧，让你事半功倍！" \
  --images cover.png card_1.png card_2.png
```

## 🔧 开发说明

### 添加自定义主题

1. 在 `assets/themes/` 目录下创建新的CSS文件
2. 参考现有主题的样式结构
3. 在渲染时使用 `-t` 参数指定新主题

### 技术栈

- **Python 3.11+** - 脚本语言
- **Playwright** - HTML转图片渲染
- **xhs库** - 小红书发布API
- **Markdown** - 内容格式

## ⚠️ 注意事项

1. Cookie有有效期限制，过期后需要重新获取
2. 发布功能需要登录小红书账号
3. 图片尺寸保持3:4比例，符合小红书推荐规格
4. 动态高度模式下图片最高4320px

## 📄 许可证

MIT License
