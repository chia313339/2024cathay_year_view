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
        st.write(f"**基本資料**")
        st.write(f"遮蔽ID: {current_id}")
        st.write(f"遮蔽姓名: {data_tmp['NAME'].values[0]}")
        st.write(f"首次接觸管道: {data_tmp['SOURCE'].values[0]}")
        tmp_data = change_date(data_tmp['FIRSTDT'].values[0])
        st.write(f"第一次接觸時間: {tmp_data}")
        tmp_data = f"{data_tmp['DAY_DIFF'].values[0]:,}"
        st.write(f"與國泰相識的日數: {tmp_data}")
        tmp_data = round(data_tmp['DAY_DIFF'].values[0] / 365, 2)
        st.write(f"相識年數: {tmp_data}")
        st.markdown(f"<br>", unsafe_allow_html=True)
        st.write(f"**靈獸分類**")
        st.markdown(f"靈獸: <span style='color: #0080FF;'>**{data_tmp['TITLE'].values[0]}**</span>", unsafe_allow_html=True)
        st.write(f"{data_tmp['DESC'].values[0]}")
        st.markdown(f"<p style='color: #ADADAD;'>{data_tmp['LOGIC'].values[0]}</p>", unsafe_allow_html=True)

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
        st.markdown(f"<br>", unsafe_allow_html=True)
        st.write(f"**FitBack資訊**")
        tmp_data = f"{data_tmp['SUM_of_STEP'].values[0]:,}"
        st.write(f"FitBack累積步數: {tmp_data}")
        tmp_data = f"{data_tmp['HIGH_LV'].values[0]:,}"
        st.write(f"FitBack最高會員等級: {data_tmp['HIGH_LV'].values[0]}")
        st.markdown(f"<p style='color: #ADADAD;'>會員等級3.4.5都是樂享家，1是探索家、2是實踐家</p>", unsafe_allow_html=True)
    with col4:
        st.write(f"**保單資訊**")
        st.write(f"是否有效契約: {data_tmp['EFT_CUST'].values[0]}")
        st.write(f"有效保單數: {data_tmp['N_POLICY_NO'].values[0]}")
        st.write(f"住院險: {data_tmp['COUNT_H_HOSPITAL'].values[0]}")
        st.write(f"手術險: {data_tmp['COUNT_S_SURGERY'].values[0]}")
        st.write(f"實支實付: {data_tmp['COUNT_R_REIMBURSEMENT'].values[0]}")
        st.write(f"重疾: {data_tmp['COUNT_M_MAJOR_ILLNESS'].values[0]}")
        st.write(f"意外: {data_tmp['COUNT_A_ACCIDENT'].values[0]}")
        st.write(f"長照: {data_tmp['COUNT_L_LONGTERM_CARE'].values[0]}")
        st.write(f"壽險: {data_tmp['COUNT_D_LIFE'].values[0]}")
        st.write(f"固定利率傳統理財: {data_tmp['COUNT_FR_FIXED_RATE'].values[0]}")
        st.write(f"變動利率傳統理財: {data_tmp['COUNT_IS_VARIABLE_RATE'].values[0]}")
        st.write(f"投資行商品: {data_tmp['COUNT_I_INVESTMENT'].values[0]}")

# Function to display a random ID
def display_random_id():
    random_index = random.randint(0, len(st.session_state.current_data_all) - 1)
    col1, col2, col3, col4 = st.columns(4)
    current_id = st.session_state.current_data_all['ID'].values[random_index]
    data_tmp = st.session_state.current_data_all[st.session_state.current_data_all['ID'] == current_id]
    with col1:
        st.write(f"**基本資料**")
        st.write(f"遮蔽ID: {current_id}")
        st.write(f"首次接觸管道: {data_tmp['SOURCE'].values[0]}")
        tmp_data = change_date(data_tmp['FIRSTDT'].values[0])
        st.write(f"第一次接觸時間: {tmp_data}")
        tmp_data = f"{data_tmp['DAY_DIFF'].values[0]:,}"
        st.write(f"與國泰相識的日數: {tmp_data}")
        tmp_data = round(data_tmp['DAY_DIFF'].values[0] / 365, 2)
        st.write(f"相識年數: {tmp_data}")
        st.markdown(f"<br>", unsafe_allow_html=True)
        st.write(f"**靈獸分類**")
        st.markdown(f"靈獸: <span style='color: #0080FF;'>**{data_tmp['TITLE'].values[0]}**</span>", unsafe_allow_html=True)
        st.write(f"{data_tmp['DESC'].values[0]}")
        st.markdown(f"<p style='color: #ADADAD;'>{data_tmp['LOGIC'].values[0]}</p>", unsafe_allow_html=True)

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
        st.markdown(f"<br>", unsafe_allow_html=True)
        st.write(f"**FitBack資訊**")
        tmp_data = f"{data_tmp['SUM_of_STEP'].values[0]:,}"
        st.write(f"FitBack累積步數: {tmp_data}")
        tmp_data = f"{data_tmp['HIGH_LV'].values[0]:,}"
        st.write(f"FitBack最高會員等級: {data_tmp['HIGH_LV'].values[0]}")
        st.markdown(f"<p style='color: #ADADAD;'>會員等級3.4.5都是樂享家，1是探索家、2是實踐家</p>", unsafe_allow_html=True)
    with col4:
        st.write(f"**保單資訊**")
        st.write(f"是否有效契約: {data_tmp['EFT_CUST'].values[0]}")
        st.write(f"有效保單數: {data_tmp['N_POLICY_NO'].values[0]}")
        st.write(f"住院險: {data_tmp['COUNT_H_HOSPITAL'].values[0]}")
        st.write(f"手術險: {data_tmp['COUNT_S_SURGERY'].values[0]}")
        st.write(f"實支實付: {data_tmp['COUNT_R_REIMBURSEMENT'].values[0]}")
        st.write(f"重疾: {data_tmp['COUNT_M_MAJOR_ILLNESS'].values[0]}")
        st.write(f"意外: {data_tmp['COUNT_A_ACCIDENT'].values[0]}")
        st.write(f"長照: {data_tmp['COUNT_L_LONGTERM_CARE'].values[0]}")
        st.write(f"壽險: {data_tmp['COUNT_D_LIFE'].values[0]}")
        st.write(f"固定利率傳統理財: {data_tmp['COUNT_FR_FIXED_RATE'].values[0]}")
        st.write(f"變動利率傳統理財: {data_tmp['COUNT_IS_VARIABLE_RATE'].values[0]}")
        st.write(f"投資行商品: {data_tmp['COUNT_I_INVESTMENT'].values[0]}")
        

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
    col01, col02, col03, col04 = st.columns(4)
    with col01:
        st.write(f"**人數統計**")
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

    with col03:
        st.write(f"**其他大盤數據**")
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack探索家：967,216、約7.38％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack實踐家：30,419、約0.23％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack樂享家：19,173、約0.15％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack有上傳步數人數：410,277、約3.13％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack平均步數：918,598.26</p>", unsafe_allow_html=True)
        st.markdown(f"<br>", unsafe_allow_html=True)
        st.write(f"**靈獸分類**")
        st.markdown(f"<p style='color: #6C6C6C;'>[C1]傲視獅鷲：40,479、約0.31％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C2]敏捷雪豹：358,301、約2.73％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C3]悠遊獨角鯨：288,095、約2.2％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C4]安逸玄武：320,820、約2.45％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C5]無懼雷鳥：185,311、約1.41％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C6]膽識鳳凰：410,699、約3.13％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C7]睿智九尾狐：402,788、約3.07％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C8]精明靈蛇：378,607、約2.89％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C9]仙境白澤：2,739,330、約20.9％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C10]共濟神狼：2,219,465、約16.94％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C11]機敏麒麟：2,832,920、約21.62％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C12]原野金羊毛獸：2,928,514、約22.35％</p>", unsafe_allow_html=True)

    with col04:
        st.write(f"**保險保障統計**(統計至2024/7)")
        st.markdown(f"<p style='color: #6C6C6C;'>有效契約客戶：7,561,963、約57.7％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有效契約保單數：21,247,121</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>平均每個有效客戶有：280.97 張表單</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>住院險客戶：3,239,709、有效客戶的42.84％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>住院保單數：3,648,006、有效保單的17.17％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>手術險客戶：1,908,350、有效客戶的25.24％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>手術保單數：2,070,115、有效保單的9.74％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>實支實付險客戶：142,847、有效客戶的1.89％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>實支實付保單數：142,847、有效保單的0.67％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>重疾險客戶：3,264,232、有效客戶的43.17％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>重疾保單數：4,092,408、有效保單的19.26％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>意外險客戶：238,930、有效客戶的3.16％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>意外險保單數：247,282、有效保單的1.16％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>長照險客戶：1,059,952、有效客戶的14.02％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>長照險保單數：1,324,178、有效保單的6.23％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>壽險客戶：2,439,548、有效客戶的32.26％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>壽險保單數：3,296,970、有效保單的15.52％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>固定利率傳統理財客戶：3,115,947、有效客戶的41.21％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>固定利率傳統理財保單數：4,604,883、有效保單的21.67％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>變動利率傳統理財客戶：917,908、有效客戶的12.14％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>變動利率傳統理財保單數：1,254,528、有效保單的5.9％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>投資型理財商品客戶：361,244、有效客戶的4.78％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>投資型理財商品保單數：565,904、有效保單的2.66％</p>", unsafe_allow_html=True)
else:
    st.title("年度回顧專案-官網會員客戶")
    st.markdown(f"<h3 style='color: #D94600;'>資料樣態</h3>", unsafe_allow_html=True)
    st.markdown('**資料區間 2023-01-01～2023-12-31，ID基底包含壽險主約要被保人、理賠檔、意外險檔、MML、官網、Fitback會員等**')
    col01, col02, col03, col04 = st.columns(4)
    with col01:
        st.write(f"**人數統計**")
        st.markdown(f"<p style='color: #6C6C6C;'>總ID數量：4,209,793</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為要保人：3,406,667、約80.92％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為被保人：3,652,791、約86.77％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為理賠事故人：1,886,642、約44.82％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經為員工：96,197、約2.29％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>曾經意外險被保人：587,216、約13.95％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>官網會員：4,209,793、約100.0％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>MML會員：2,757,904、約65.51％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack會員：1,127,688、約26.79％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有旅平險：136,804、約3.25％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>至少一項服務通路：4,013,680、約95.34％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>什麼都沒有的人(沒旅平沒會員沒MML沒FitBack沒服務軌跡)：0、約0.0％</p>", unsafe_allow_html=True)

    with col02:
        st.write(f"**各通路接觸次數**")
        st.markdown(f"<p style='color: #6C6C6C;'>有業務員服務：2,451,426、約58.23％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有直效服務：748,199、約17.77％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有服務中心櫃台服務：164,897、約3.92％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有官網服務：740,873、約17.6％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有MML服務：2,444,878、約58.08％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有電話_0800服務：388,760、約9.23％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有電話_0900服務：271,529、約6.45％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有簡訊服務：2,491,612、約59.19％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有停效催繳提醒服務：725,844、約17.24％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有MAIL HUNTER服務：3,542,588、約84.15％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有BILL HUNTER服務：2,504,777、約59.5％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有LINE服務：67,316、約1.6％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有行銷網站服務：75,279、約1.79％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有紙本通知服務：1,492,005、約35.44％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有放款業務服務：442,021、約10.5％</p>", unsafe_allow_html=True)


    with col03:
        st.write(f"**其他大盤數據**")
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack探索家：961,691、約22.84％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack實踐家：30,222、約0.72％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack樂享家：19,132、約0.45％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack有上傳步數人數：409,552、約9.73％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>FitBack平均步數：919,260.72</p>", unsafe_allow_html=True)
        st.markdown(f"<br>", unsafe_allow_html=True)
        st.write(f"**靈獸分類**")
        st.markdown(f"<p style='color: #6C6C6C;'>[C1]傲視獅鷲：40,263、約0.96％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C2]敏捷雪豹：320,578、約7.62％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C3]悠遊獨角鯨：269,842、約6.41％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C4]安逸玄武：309,888、約7.36％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C5]無懼雷鳥：107,605、約2.56％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C6]膽識鳳凰：271,422、約6.45％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C7]睿智九尾狐：232,851、約5.53％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C8]精明靈蛇：306,081、約7.27％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C9]仙境白澤：546,033、約12.97％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C10]共濟神狼：583,005、約13.85％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C11]機敏麒麟：601,174、約14.28％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>[C12]原野金羊毛獸：621,051、約14.75％</p>", unsafe_allow_html=True)

    with col04:
        st.write(f"**保險保障統計**(統計至2024/7)")
        st.markdown(f"<p style='color: #6C6C6C;'>有效契約客戶：3,273,088、約77.75％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>有效契約保單數：11,647,585</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>平均每個有效客戶有：355.86 張表單</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>住院險客戶：1,585,163、有效客戶的48.43％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>住院保單數：1,861,448、有效保單的15.98％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>手術險客戶：958,379、有效客戶的29.28％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>手術保單數：1,049,547、有效保單的9.01％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>實支實付險客戶：101,713、有效客戶的3.11％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>實支實付保單數：101,713、有效保單的0.87％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>重疾險客戶：1,635,324、有效客戶的49.96％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>重疾保單數：2,196,308、有效保單的18.86％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>意外險客戶：137,379、有效客戶的4.2％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>意外險保單數：143,564、有效保單的1.23％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>長照險客戶：636,220、有效客戶的19.44％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>長照險保單數：842,975、有效保單的7.24％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>壽險客戶：1,267,616、有效客戶的38.73％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>壽險保單數：1,877,683、有效保單的16.12％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>固定利率傳統理財客戶：1,452,520、有效客戶的44.38％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>固定利率傳統理財保單數：2,396,540、有效保單的20.58％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>變動利率傳統理財客戶：536,180、有效客戶的16.38％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>變動利率傳統理財保單數：788,736、有效保單的6.77％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>投資型理財商品客戶：232,135、有效客戶的7.09％</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #6C6C6C;'>投資型理財商品保單數：389,071、有效保單的3.34％</p>", unsafe_allow_html=True)




st.markdown('---')
st.markdown(f"<h3 style='color: #D94600;'>測試資料</h3>", unsafe_allow_html=True)

button_row = row(6, vertical_align="left")

if button_row.button('隨機示範ID'):
    display_director()
    st.session_state.index = (st.session_state.index + 1) % len(st.session_state.data['ID'])

if button_row.button('隨機母體POOL'):
    display_random_id()


