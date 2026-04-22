import pandas as pd
import os

DATA_DIR = "data/raw/岗位表"
SCORE_DIR = "data/raw/进面分数线"
CACHE_DIR = "data/cache"

# 创建缓存目录
os.makedirs(CACHE_DIR, exist_ok=True)

print("=" * 60)
print("开始预加载数据...")
print("=" * 60)

# 1. 预加载岗位表数据
print("\n📋 处理岗位表数据...")
files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".xlsx")])

for file in files:
    year = file.replace(".xlsx", "")
    print(f"\n处理 {year}年...")
    
    file_path = os.path.join(DATA_DIR, file)
    xl = pd.ExcelFile(file_path)
    
    # 加载并合并所有工作表
    all_dfs = []
    for sheet in xl.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet, header=1)
        df['工作表'] = sheet
        all_dfs.append(df)
    
    merged_df = pd.concat(all_dfs, ignore_index=True)
    
    # 删除不需要的列
    columns_to_drop = ["部门网站", "咨询电话1", "咨询电话2", "咨询电话3", "落户地点", "学位", "招录机关", "工作表"]
    for col in columns_to_drop:
        if col in merged_df.columns:
            merged_df = merged_df.drop(columns=[col])
    
    # 保存为Parquet
    cache_path = os.path.join(CACHE_DIR, f"positions_{year}.parquet")
    merged_df.to_parquet(cache_path, index=False)
    print(f"  ✓ 已保存: {cache_path} ({len(merged_df)} 行)")

# 2. 预加载进面分数线数据
print("\n📊 处理进面分数线数据...")
score_file = os.path.join(SCORE_DIR, "国考18-26年进面分数线.xlsx")

if os.path.exists(score_file):
    xl = pd.ExcelFile(score_file)
    all_scores = []
    
    for sheet_name in xl.sheet_names:
        df = pd.read_excel(score_file, sheet_name=sheet_name)
        # 从工作表名称中提取年份
        year = None
        for y in range(2018, 2027):
            if str(y) in sheet_name:
                year = y
                break
        if year:
            df['年份'] = year
            all_scores.append(df)
    
    if all_scores:
        score_df = pd.concat(all_scores, ignore_index=True)
        
        # 保存为Parquet
        cache_path = os.path.join(CACHE_DIR, "scores.parquet")
        score_df.to_parquet(cache_path, index=False)
        print(f"  ✓ 已保存: {cache_path} ({len(score_df)} 行)")

print("\n" + "=" * 60)
print("✅ 预加载完成！")
print(f"📁 缓存文件保存在: {os.path.abspath(CACHE_DIR)}")
print("=" * 60)
