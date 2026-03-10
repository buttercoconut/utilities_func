def split_by_newline_with_limit(text: str, limit: int = 500) -> list[str]:
    """
    주어진 문자열을 줄바꿈(n) 단위로 분리한 뒤,
    각 청크가 `limit`(기본값 500)자를 넘지 않도록 분할한다.

    Parameters
    ----------
    text : str
        분할하고자 하는 긴 코드 문자열.
    limit : int, optional
        한 청크당 허용되는 최대 길이. 기본값은 500.

    Returns
    -------
    list[str]
        길이 제한을 만족하도록 분할된 청크들의 리스트.
    """
    if not text:
        return []

    # 줄 단위(줄바꿈 포함)로 분리
    lines = text.splitlines(True)  # True → 줄바꿈 문자도 함께 남김
    chunks = []          # 최종 결과
    current_chunk = []   # 현재 청크에 모아지는 줄들
    current_len = 0      # 현재 청크의 길이

    for line in lines:
        line_len = len(line)

        # 현재 줄을 넣으면 한도를 초과하지 않으면 그대로 추가
        if current_len + line_len <= limit:
            current_chunk.append(line)
            current_len += line_len
            continue

        # 현재 청크를 저장
        if current_chunk:
            chunks.append(.join(current_chunk))

        # 한 줄 자체가 limit을 넘는 경우
        if line_len > limit:
            # 줄을 limit 단위로 분할
            start = 0
            while start < line_len:
                end = min(start + limit, line_len)
                chunks.append(line[start:end])
                start = end
            # 다음 줄부터 새 청크를 시작
            current_chunk = []
            current_len = 0
        else:
            # 새 청크를 시작하고 현재 줄을 넣음
            current_chunk = [line]
            current_len = line_len

    # 마지막 청크를 추가
    if current_chunk:
        chunks.append(.join(current_chunk))

    return chunks


# ------------------------------------------------------------------
# 예시 사용법
# ------------------------------------------------------------------
if __name__ == "__main__":
    # 500자를 조금 넘는 예시 문자열 (줄마다 100자)
    example = "\n".join([f"Line {i+1}: " + "x" * 97 for i in range(12)])
    # 총 길이: 12줄 × (len(Line i: ) + 97) ≈ 12×103 ≈ 1236

    result = split_by_newline_with_limit(example, limit=500)

    for idx, chunk in enumerate(result, 1):
        print(f"--- Chunk {idx} ({len(chunk)}자) ---")
        print(chunk)
        print()
