import streamlit as st
import pandas as pd
from streamlit_extras.row import row
from datetime import datetime
import random

def change_date(date_string):
    date_obj = datetime.strptime(date_string, '%d%b%Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date

# Load the CSV files once and store in session state
if 'data' not in st.session_state:
    st.session_state.data = pd.read_csv('ABT_S.csv')
    st.session_state.data_all = pd.read_csv('ABT_T.csv')
    st.session_state.data_all_2 = pd.read_csv('ABT_T2.csv')
    st.session_state.current_data_all = st.session_state.data_all
    st.session_state.is_full_data = True
    st.session_state.index = 0

# 确保 session state 已初始化
if 'is_full_data' not in st.session_state:
    st.session_state.is_full_data = True

# 設置頁面配置
st.set_page_config(layout="wide")

# Function to display data for the current ID in order
def display_director():
    col1, col2, col3, col4 = st.columns(4)
    current_id = st.session_state.data['ID'].values[st.session_state.index]
    data_tmp = st.session_state.data[st.session_state.data['ID'] == current_id]
    with col1:
        st.write(f"**遮蔽ID:** {current_id}")
        st.write(f"**姓名:** {data_tmp['NAME'].values[0]}")
        st.write(f"**首次接觸管道:** {data_tmp['SOURCE'].values[0]}")
        tmp_data = change_date(data_tmp['FIRSTDT'].values[0])
        st.write(f"**第一次接觸時間:** {tmp_data}")
        tmp_data = f"{data_tmp['DAY_DIFF'].values[0]:,}"
        st.write(f"**與國泰相識的日數:** {tmp_data}")
        tmp_data = round(data_tmp['DAY_DIFF'].values[0] / 365, 2)
        st.write(f"**相識年數:** {tmp_data}")
    with col2:
        tmp_data = data_tmp['A01'].values[0] + data_tmp['A02'].values[0]
        st.write(f"**各通路接觸次數**")
        st.write(f"業務員: {tmp_data}")
        st.write(f"直效: {data_tmp['A03'].values[0]}")
        st.write(f"服務中心櫃台: {data_tmp['A05'].values[0]}")
        st.write(f"官網: {data_tmp['A07'].values[0]}")
        st.write(f"MML: {data_tmp['A08'].values[0]}")
        st.write(f"電話_0800: {data_tmp['A09'].values[0]}")
        st.write(f"電話_0900: {data_tmp['A10'].values[0]}")
        st.write(f"簡訊: {data_tmp['A13'].values[0]}")
        st.write(f"停效催繳提醒: {data_tmp['A15'].values[0]}")
        st.write(f"MAIL HUNTER: {data_tmp['A17'].values[0]}")
        st.write(f"BILL HUNTER: {data_tmp['A18'].values[0]}")
        st.write(f"LINE: {data_tmp['A19'].values[0]}")
        st.write(f"行銷網站: {data_tmp['A21'].values[0]}")
        st.write(f"紙本通知: {data_tmp['A24'].values[0]}")
        st.write(f"放款業務: {data_tmp['A99'].values[0]}")
    with col3:
        st.write(f"**旅平險資訊**")
        st.write(f"最常去的國家: {data_tmp['MAX_RGN_PLACE'].values[0]}")
        st.write(f"最常去的國家日數: {data_tmp['MAX_ISSUE_DAYS'].values[0]}")
        st.write(f"累積總旅遊日數: {data_tmp['SUM_ISSUE_DAYS'].values[0]}")
    with col4:
        tmp_data = f"{data_tmp['SUM_of_STEP'].values[0]:,}"
        st.write(f"**FitBack累積步數:** {tmp_data}")
        tmp_data = f"{data_tmp['HIGH_LV'].values[0]:,}"
        st.write(f"**FitBack最高會員等級:** {data_tmp['HIGH_LV'].values[0]}")
        st.write(f"會員等級3.4.5都是樂享家，1是探索家、2是實踐家")

# Function to display a random ID
def display_random_id():
    random_index = random.randint(0, len(st.session_state.current_data_all) - 1)
    col1, col2, col3, col4 = st.columns(4)
    current_id = st.session_state.current_data_all['ID'].values[random_index]
    data_tmp = st.session_state.current_data_all[st.session_state.current_data_all['ID'] == current_id]
    with col1:
        st.write(f"**遮蔽ID:** {current_id}")
        st.write(f"**首次接觸管道:** {data_tmp['SOURCE'].values[0]}")
        tmp_data = change_date(data_tmp['FIRSTDT'].values[0])
        st.write(f"**第一次接觸時間:** {tmp_data}")
        tmp_data = f"{data_tmp['DAY_DIFF'].values[0]:,}"
        st.write(f"**與國泰相識的日數:** {tmp_data}")
        tmp_data = round(data_tmp['DAY_DIFF'].values[0] / 365, 2)
        st.write(f"**相識年數:** {tmp_data}")
    with col2:
        tmp_data = data_tmp['A01'].values[0] + data_tmp['A02'].values[0]
        st.write(f"**各通路接觸次數**")
        st.write(f"業務員: {tmp_data}")
        st.write(f"直效: {data_tmp['A03'].values[0]}")
        st.write(f"服務中心櫃台: {data_tmp['A05'].values[0]}")
        st.write(f"官網: {data_tmp['A07'].values[0]}")
        st.write(f"MML: {data_tmp['A08'].values[0]}")
        st.write(f"電話_0800: {data_tmp['A09'].values[0]}")
        st.write(f"電話_0900: {data_tmp['A10'].values[0]}")
        st.write(f"簡訊: {data_tmp['A13'].values[0]}")
        st.write(f"停效催繳提醒: {data_tmp['A15'].values[0]}")
        st.write(f"MAIL HUNTER: {data_tmp['A17'].values[0]}")
        st.write(f"BILL HUNTER: {data_tmp['A18'].values[0]}")
        st.write(f"LINE: {data_tmp['A19'].values[0]}")
        st.write(f"行銷網站: {data_tmp['A21'].values[0]}")
        st.write(f"紙本通知: {data_tmp['A24'].values[0]}")
        st.write(f"放款業務: {data_tmp['A99'].values[0]}")
    with col3:
        st.write(f"**旅平險資訊**")
        st.write(f"最常去的國家: {data_tmp['MAX_RGN_PLACE'].values[0]}")
        st.write(f"最常去的國家日數: {data_tmp['MAX_ISSUE_DAYS'].values[0]}")
        st.write(f"累積總旅遊日數: {data_tmp['SUM_ISSUE_DAYS'].values[0]}")
    with col4:
        tmp_data = f"{data_tmp['SUM_of_STEP'].values[0]:,}"
        st.write(f"**FitBack累積步數:** {tmp_data}")
        tmp_data = f"{data_tmp['HIGH_LV'].values[0]:,}"
        st.write(f"**FitBack最高會員等級:** {data_tmp['HIGH_LV'].values[0]}")
        st.write(f"會員等級3.4.5都是樂享家，1是探索家、2是實踐家")

# Streamlit app
button_label = '切換官網會員資料' if st.session_state.is_full_data else '切換全客戶資料'
if st.button(button_label):
    st.session_state.is_full_data = not st.session_state.is_full_data
    st.session_state.current_data_all = st.session_state.data_all if st.session_state.is_full_data else st.session_state.data_all_2
    st.session_state.index = 0  # Reset the index to 0 when switching datasets
    st.experimental_rerun()  # Immediately rerun to update the button label

if st.session_state.is_full_data:
    st.title("年度回顧專案-全客戶")
    st.markdown(f"<h3 style='color: #D94600;'>資料樣態</h3>", unsafe_allow_html=True)
    st.markdown('**資料區間 2023-01-01～2023-12-31，ID基底包含壽險主約要被保人、理賠檔、意外險檔、MML、官網、Fitback會員等**')
    col01, col02, col03, col4 = st.columns(4)
    with col01:
        st.markdown(f"<p style='color: #6C6C6C;'>總ID數量：13,105,329</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為要保人：7,986,621、約60.94％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為被保人：10,544,910、約80.46％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為理賠事故人：5,130,941、約39.15％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為員工：107,592、約0.82％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經意外險被保人：1,877,612、約14.33％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>官網會員：4,209,793、約32.12％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>MML會員：2,784,178、約21.24％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack會員：1,133,651、約8.65％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有旅平險：222,054、約1.69％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>至少一項服務通路：7,461,738、約56.94％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>什麼都沒有的人(沒旅平沒會員沒MML沒FitBack沒服務軌跡)：5,400,363、約41.21％</p>", unsafe_allow_html=True)
    with col02:
        st.write(f"**保險保障統計**(統計至7/1)")
        st.markdown(f"<p style='color: #6C6C6C;'>有效契約客戶：7,561,963、約57.7％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有效契約保單數：21,247,121</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>平均每個有效客戶有：280.97 張表單</p>", unsafe_allow_html=True)

    with col03:
        st.write(f"**各通路接觸次數**")
        st.markdown(f"<p style='color: #6C6C6C;'>有業務員服務：4,683,466、約35.74％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有直效服務：1,076,920、約8.22％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有服務中心櫃台服務：212,640、約1.62％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有官網服務：755,690、約5.77％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有MML服務：2,458,733、約18.76％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有電話_0800服務：553,054、約4.22％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有電話_0900服務：366,553、約2.8％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有簡訊服務：4,603,978、約35.13％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有停效催繳提醒服務：1,370,596、約10.46％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有MAIL HUNTER服務：4,096,747、約31.26％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有BILL HUNTER服務：3,081,018、約23.51％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有LINE服務：72,415、約0.55％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有行銷網站服務：84,611、約0.65％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有紙本通知服務：2,912,867、約22.23％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有放款業務服務：453,609、約3.46％</p>", unsafe_allow_html=True)

    with col04:
        st.write(f"**其他大盤數據**")
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack探索家：967,216、約7.38％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack實踐家：30,419、約0.23％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack樂享家：19,173、約0.15％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack有上傳步數人數：410,277、約3.13％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack平均步數：918,598.26</p>", unsafe_allow_html=True)
else:
    st.title("年度回顧專案-官網會員客戶")
    st.markdown(f"<h3 style='color: #D94600;'>資料樣態</h3>", unsafe_allow_html=True)
    st.markdown('**資料區間 2023-01-01～2023-12-31，ID基底包含壽險主約要被保人、理賠檔、意外險檔、MML、官網、Fitback會員等**')
    col01, col02, col03 = st.columns(3)
    with col01:
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>總ID數量：4,167,135</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>曾經為要保人：3,380,125、約81.11％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>曾經為被保人：3,620,522、約86.88％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>曾經為理賠事故人：1,866,398、約44.79％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>曾經為員工：95,730、約2.3％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>曾經意外險被保人：587,866、約14.11％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>官網會員：4,167,135、約100.0％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>MML會員：2,712,877、約65.1％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>FitBack會員：1,097,939、約26.35％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有旅平險：136,318、約3.27％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>至少一項服務通路：3,991,698、約95.79％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>什麼都沒有的人(沒旅平沒會員沒MML沒FitBack沒服務軌跡)：0、約0.0％</p>", unsafe_allow_html=True)

    with col02:
        st.write(f"**各通路接觸次數**")
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有業務員服務：2,436,773、約58.48％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有直效服務：743,946、約17.85％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有服務中心櫃台服務：164,708、約3.95％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有官網服務：740,759、約17.78％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有MML服務：2,423,043、約58.15％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有電話_0800服務：387,633、約9.3％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有電話_0900服務：270,547、約6.49％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有簡訊服務：2,478,018、約59.47％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有停效催繳提醒服務：722,882、約17.35％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有MAIL HUNTER服務：3,536,693、約84.87％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有BILL HUNTER服務：2,498,621、約59.96％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有LINE服務：67,249、約1.61％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有行銷網站服務：75,125、約1.8％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有紙本通知服務：1,483,021、約35.59％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>有放款業務服務：442,038、約10.61％</p>", unsafe_allow_html=True)


    with col03:
        st.write(f"**其他大盤數據**")
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>FitBack樂想家：941,735、約22.6％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>FitBack探索家：29,684、約0.71％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>FitBack實踐家：39,773、約0.95％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>FitBack有上傳步數人數：409,595、約9.83％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C; margin-bottom: 5px;'>FitBack平均步數：919,251.43</p>", unsafe_allow_html=True)




st.markdown('---')
st.markdown(f"<h3 style='color: #D94600;'>測試資料</h3>", unsafe_allow_html=True)

button_row = row(6, vertical_align="left")

if button_row.button('隨機示範ID'):
    display_director()
    st.session_state.index = (st.session_state.index + 1) % len(st.session_state.data['ID'])

if button_row.button('隨機母體POOL'):
    display_random_id()


