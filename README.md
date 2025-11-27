# Intimate Moments - 亲密时刻

伴侣健康追踪应用官方网站

## 页面结构

```
docs/
├── index.html        # 中文主页
├── index-en.html     # 英文主页
├── privacy.html      # 隐私政策（中英双语）
├── terms.html        # 使用条款
├── support.html      # 帮助与支持
└── README.md         # 说明文档
```

## 部署到 GitHub Pages

### 步骤 1: 创建 GitHub 仓库

如果还没有仓库，在 GitHub 上创建一个新仓库，例如 `intimate-moments-website`

### 步骤 2: 上传文件

```bash
cd /path/to/亲密时刻/docs
git init
git add .
git commit -m "Initial website commit"
git branch -M main
git remote add origin https://github.com/liyifenggit/intimate-moments-website.git
git push -u origin main
```

### 步骤 3: 启用 GitHub Pages

1. 进入仓库的 **Settings** → **Pages**
2. **Source** 选择 `Deploy from a branch`
3. **Branch** 选择 `main`，文件夹选择 `/ (root)`
4. 点击 **Save**

### 步骤 4: 访问网站

部署完成后，网站地址为：
```
https://liyifenggit.github.io/intimate-moments-website/
```

## App Store 提交信息

### 隐私政策 URL
```
https://liyifenggit.github.io/intimate-moments-website/privacy.html
```

### 支持 URL
```
https://liyifenggit.github.io/intimate-moments-website/support.html
```

### 营销 URL（可选）
```
https://liyifenggit.github.io/intimate-moments-website/
```

## 自定义域名（可选）

如果有自己的域名，可以：

1. 在 `docs/` 目录下创建 `CNAME` 文件，内容为你的域名：
   ```
   intimatemoments.app
   ```

2. 在域名 DNS 设置中添加：
   - **类型**: CNAME
   - **名称**: www（或 @）
   - **值**: liyifenggit.github.io

## 更新网站

修改文件后：
```bash
git add .
git commit -m "Update website"
git push
```

GitHub Pages 会自动重新部署。

## 联系方式

- Email: support@intimatemoments.app
- GitHub: https://github.com/liyifenggit

---

© 2025 Intimate Moments. All rights reserved.
