import json

path = r'C:\Users\zcris\Desktop\Introduction_Transformers\PositionEmbeddings.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Search for all occurrences to replace
for i, c in enumerate(nb['cells']):
    src = c['source']
    for j, line in enumerate(src):
        # Replace "I saw her duck" / "I saw her duck" variations
        line = line.replace('I saw her duck', 'Lily is running along the river bank')
        line = line.replace('duck her saw I', 'bank river the along running is Lily')
        # Also handle token list references
        line = line.replace('["I", "saw", "her", "duck"]', '["Lily", "is", "running", "along"]')
        line = line.replace('\"I\", \"saw\", \"her\", \"duck\"', '"Lily", "is", "running", "along"')
        # Handle the tokens list in code
        line = line.replace("tokens = [\"I\", \"saw\", \"her\", \"duck\"]", "tokens = [\"Lily\", \"is\", \"running\", \"along\"]")
        # Replace standalone "I saw her duck" references
        line = line.replace('\"I saw her duck\"', '"Lily is running along the river bank"')
        line = line.replace("\"I saw her duck\"", "\"Lily is running along the river bank\"")
        line = line.replace('\\\"I saw her duck\\\"', '\\\"Lily is running along the river bank\\\"')
        # Replace the 4-token id lists
        line = line.replace('torch.tensor([0, 1, 2, 3])  # I saw her duck', 'torch.tensor([0, 1, 2, 3])  # Lily is running along')
        line = line.replace('torch.tensor([3, 2, 1, 0])  # duck her saw I', 'torch.tensor([3, 2, 1, 0])  # along running is Lily')
        line = line.replace('# 假设这四个 token 在词表里的编号就是 0,1,2,3', '# Lily/is/running/along 在词表中的编号 0,1,2,3')
        # Replace in comments
        line = line.replace('一个极小句子，用来观察位置编码如何工作', '截取前 4 个词，用来观察位置编码如何工作')
        # The proof section
        line = line.replace('"I saw her duck" 和 "duck her saw I" 的 attention 权重完全相同', '"Lily is running along" 和 "along running is Lily" 的 attention 权重完全相同')
        # Output labels
        line = line.replace('Attention weights for \\\"I saw her duck\\\"', 'Attention weights for \\\"Lily is running along\\\"')
        line = line.replace('Attention weights for \\\"duck her saw I\\\"', 'Attention weights for \\\"along running is Lily\\\"')
        # Replace the markdown proof statement
        line = line.replace('"I saw her duck" 和 "duck her saw I" 的 attention 权重完全相同（只是行/列顺序不同）。', '"Lily is running along" 和 "along running is Lily" 的 attention 权重完全相同（只是行/列顺序不同）。')
        # The "I saw her duck" vector display
        line = line.replace('"I saw her duck" 的输入向量', '"Lily is running along" 的输入向量')
        src[j] = line

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('Done. All replacements applied.')
