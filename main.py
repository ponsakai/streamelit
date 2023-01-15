import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

#スライダー
# condition = st.slider('あなたの調子は？',0, 100, 50)
# 'コンディション',condition

# #text入力
# text = st.text_input('あなたの趣味を教えんかい')
# 'あなたの趣味は',text,'です'

#選択肢と表示
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option, 'です'

#画像の表示
# if st.checkbox('Show Image'):
#     img = Image.open('/Users/sakaitakeshiryou/Desktop/sample.py/web_application/maron.jpg')
#     st.image(img, caption='maron', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],#縦に100横に2の乱数を作成しそれぞれ50で割った物に新宿の緯度経度を足す
#     columns=['lat','lon']
# )


#st.dataframe(df.style.highlight_max(axis=0))#, width=100, height=100)#st.writeだと高さ幅を変えられない axis=0は行
# st.table(df.style.highlight_max(axis=0))#静的
# st.bar_chart(df) #line, areも可能
# st.map(df)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


