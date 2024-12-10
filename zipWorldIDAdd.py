import os
import json
import re
from glob import glob

# zipWorldList.json 파일 로드
with open("zipWorldList.json", "r", encoding="utf-8") as zip_file:
    zip_data = json.load(zip_file)

# 탐색할 폴더
folders = ["apple", "korea", "youtube", "spotify"]

# 문자열 정규화를 위한 함수 (괄호 제거, 소문자 변환, 공백 제거)
def normalize_text(text):
    if text:
        # 괄호와 내용을 제거한 뒤 공백 제거 및 소문자 변환
        text = re.sub(r"\s*\(.*?\)\s*", " ", text).strip()
        return re.sub(r"\s+", "", text.lower())
    return ""

# zipWorldList 데이터를 사전으로 변환하여 빠르게 검색 가능하도록 변경
zip_lookup = {}
for item in zip_data:
    key = (normalize_text(item["title"]), normalize_text(item["artist"]))
    zip_lookup[key] = {
        "appleID": item.get("appleID"),
        "youtubeID": item.get("youtubeID"),
        "spotifyID": item.get("spotifyID")
    }

# 각 폴더 순회
for folder in folders:
    json_files = glob(os.path.join(folder, "**", "*.json"), recursive=True)
    
    for file_path in json_files:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                updated_data = []
                for item in data:
                    # 폴더 안 데이터의 제목과 아티스트를 정규화
                    normalized_title = normalize_text(item.get("title"))
                    normalized_artist = normalize_text(item.get("artist"))
                    key = (normalized_title, normalized_artist)
                    
                    # zip_lookup에서 매칭되는 데이터가 있다면 ID 추가
                    if key in zip_lookup:
                        ids = zip_lookup[key]
                        # 각 ID를 확인하고 존재하면 추가
                        if ids.get("appleID"):
                            item["appleID"] = ids["appleID"]
                        if ids.get("youtubeID"):
                            item["youtubeID"] = ids["youtubeID"]
                        if ids.get("spotifyID"):
                            item["spotifyID"] = ids["spotifyID"]
                    updated_data.append(item)

                # 변경된 데이터를 파일에 다시 저장
                with open(file_path, "w", encoding="utf-8") as out_file:
                    json.dump(updated_data, out_file, ensure_ascii=False, indent=4)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {file_path}: {e}")

print("모든 폴더의 JSON 파일이 업데이트되었습니다.")
