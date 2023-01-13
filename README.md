# MFT2022_Clock
Maker Fair Tokyo2022で出展販売したローリングクロックのデータ保存場所  

～フォルダ/ファイル説明～  
/3D_Laser_cutter																：外装（レーザーカッター加工データ）  
/3D_printer(FDM)																：本体（3Dプリンタ出力データ）  
20221019_step_motor_SW_use_(intrpt-timer).py		：プログラム（Python）  
README.md																				：本ファイル  
assembling instructions.pdf											：外装と本体の組立手順  
step_motor_cirkit_ブレッドボード.pdf							：ブレットボード配線図  
step_motor_cirkit_回路図.pdf											：回路図  
ローリングクロックプログラム説明書(timer割込み.pdf	：プログラム説明書  

【参考】  
本プログラムは以下の構成で実施しています  
制御基板：RaspberryPi pico（MicroPython）
モーター：ステッピングモータ”28BYJ-48”  
ドライバ：ULN2003  
※モーターとドライバのセット品をAliExpressで購入  
