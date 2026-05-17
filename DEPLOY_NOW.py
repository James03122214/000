# -*- coding: utf-8 -*-
"""
台股處置股預警系統 - 雲端部署準備腳本
此腳本會幫您準備所有雲端部署所需的檔案
"""

import os
import shutil
import sys

def prepare_deployment_files():
    """準備雲端部署所需檔案"""
    
    print("=" * 60)
    print("🚀 台股處置股預警系統 - 雲端部署準備")
    print("=" * 60)
    
    # 檢查必要檔案
    required_files = [
        "cloud_app.py",
        "requirements.txt",
        "README.md",
        ".streamlit/config.toml"
    ]
    
    print("\n📋 檢查必要檔案...")
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - 缺少")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ 缺少必要檔案: {missing_files}")
        return False
    
    print("\n✅ 所有必要檔案都已準備完成！")
    
    # 建立部署資料夾
    deploy_folder = "deployment_package"
    if os.path.exists(deploy_folder):
        shutil.rmtree(deploy_folder)
    os.makedirs(deploy_folder)
    
    # 複製檔案到部署資料夾
    print(f"\n📦 複製檔案到部署資料夾: {deploy_folder}")
    
    files_to_copy = [
        "cloud_app.py",
        "requirements.txt", 
        "README.md",
        ".streamlit/config.toml"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            dest = os.path.join(deploy_folder, file)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(file, dest)
            print(f"✅ 已複製: {file}")
    
    print(f"\n✅ 部署檔案已準備完成在 '{deploy_folder}' 資料夾中")
    
    # 顯示部署步驟
    print("\n" + "=" * 60)
    print("🌐 雲端部署步驟 (Streamlit Cloud)")
    print("=" * 60)
    
    print("\n📝 步驟 1: 建立 GitHub 帳號和 Repository")
    print("   1. 前往 https://github.com 註冊帳號")
    print("   2. 點擊 '+' → 'New repository'")
    print("   3. 輸入 repository 名稱 (建議: stock-alert-system)")
    print("   4. 選擇 'Public' 或 'Private'")
    print("   5. 點擊 'Create repository'")
    
    print("\n📤 步驟 2: 上傳檔案到 GitHub")
    print("   1. 在 GitHub repository 頁面，點擊 'uploading an existing file'")
    print("   2. 將 'deployment_package' 資料夾中的所有檔案拖曳上傳")
    print("   3. 確保上傳:")
    print("      - cloud_app.py")
    print("      - requirements.txt")
    print("      - README.md")
    print("      - .streamlit/config.toml")
    print("   4. 點擊 'Commit changes'")
    
    print("\n🚀 步驟 3: 部署到 Streamlit Cloud")
    print("   1. 前往 https://streamlit.io/cloud")
    print("   2. 點擊 'Sign up' 或 'Log in'")
    print("   3. 使用 GitHub 帳號登入")
    print("   4. 點擊 'New app'")
    print("   5. 選擇您的 GitHub repository")
    print("   6. 選擇分支 (通常是 'main' 或 'master')")
    print("   7. 確認 main file path 為 'cloud_app.py'")
    print("   8. 點擊 'Deploy'")
    
    print("\n⏳ 步驟 4: 等待部署完成")
    print("   - 部署通常需要 2-5 分鐘")
    print("   - 您可以在 Streamlit Cloud 頁面看到部署進度")
    print("   - 完成後會顯示應用程式網址")
    
    print("\n🎉 步驟 5: 測試您的網站")
    print("   - 點擊提供的網址")
    print("   - 測試股票代碼輸入功能")
    print("   - 確認所有功能正常運作")
    
    print("\n" + "=" * 60)
    print("📱 您的網站網址格式:")
    print("https://your-app-name.streamlit.app")
    print("=" * 60)
    
    print("\n💡 提示:")
    print("   - 部署後，程式碼更新會自動重新部署")
    print("   - 免費版每月有 750 小時運行時間")
    print("   - 支援 HTTPS 和 SSL 憑證")
    
    print("\n📚 詳細部署指南請參考: CLOUD_DEPLOYMENT_GUIDE.md")
    
    return True

def main():
    """主程式"""
    try:
        success = prepare_deployment_files()
        if success:
            print("\n✅ 部署準備完成！請按照上述步驟進行雲端部署。")
        else:
            print("\n❌ 部署準備失敗，請檢查缺少的檔案。")
    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
    
    input("\n按 Enter 鍵退出...")

if __name__ == "__main__":
    main()
