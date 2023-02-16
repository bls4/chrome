wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb;
dpkg -i google-chrome-stable_current_amd64.deb;
rm -rf google-chrome-stable_current_amd64.deb;
apt --fix-broken install;
sed -i "s|Exec=/usr/bin/google-chrome-stable %U|Exec=/usr/bin/google-chrome-stable %U --no-sandbox --disable-dev-shm-usage --disable-gpu|g" /usr/share/applications/google-chrome.desktop;
wget -P /root/.config https://raw.githubusercontent.com/bls4/chrome/main/google-chrome.zip;
unzip /root/.config/google-chrome.zip;
rm -rf /root/.config/google-chrome/vtope/*;
wget -P /root/.config/google-chrome/vtope https://nextgensoft.ru/bots/youbot/youbot_chrome.zip;
unzip /root/.config/google-chrome/vtope/youbot_chrome.zip
