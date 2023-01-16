def eevee_generator():
    yield "イーブイ"
    yield "シャワーズ"
    yield "サンダース"
    yield "ブースター"
    yield "エーフィ"
    yield "ブラッキー"
    yield "リーフィア"
    yield "グレイシア"
    yield "ニンフィア"

eevee_iter = eevee_generator()
print(next(eevee_iter))

for _ in range(3): 
    print(f"<{next(eevee_iter)}>")

for item in eevee_iter: 
    print(f"[{item}]")

print(next(eevee_iter))
