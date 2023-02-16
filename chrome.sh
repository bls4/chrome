wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb;
dpkg -i google-chrome-stable_current_amd64.deb;
rm -rf google-chrome-stable_current_amd64.deb;
apt --fix-broken install;
sed -i "s|Exec=/usr/bin/google-chrome-stable %U|Exec=/usr/bin/google-chrome-stable %U --no-sandbox --disable-dev-shm-usage --disable-gpu|g" /usr/share/applications/google-chrome.desktop
