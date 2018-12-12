Name:          harbour-themepack-nunito
Version:       0.0.1
Release:       1
Summary:       Nunito font pack
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      harbour-themepacksupport >= 0.0.8-1
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
Nunito package for Theme pack support for Sailfish OS.

%files
%defattr(-,root,root,-)
/usr/share/*

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/harbour-themepack-{name}
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
fi
fi

%changelog
* Wed Dec 12 2018 0.0.1
- First build.
