Linux Commands
-   Adding to `$PATH`: `export $PATH="$PATH:/path/to/add"`
-   Using grep

    -   to search all files and folders:* grep -r word dir-name*
    -   see [here](https://askubuntu.com/questions/1164743/how-to-use-grep-to-search-through-the-help-output) on how to search the output `--help`
    -   Multiple patterns: `grep 'pattern1|pattern2' file`
    -   `grep -- -patternBeginningWithHyphen file` to [search for patterns that begin with hyphen](https://askubuntu.com/questions/1164743/how-to-use-grep-to-search-through-the-help-output)

-   To run shell script

*chmod +x /path/to/yourscript.sh*

*/path/to/yourscript.sh*

-   Change to root

*sudo -i*

-   Delete files from usr/local

*cd /usr/local/src*

* sudo rm ./file-name (rm -r to delete the entire folder)*

-   **Deleting all files**

*rm -i dir/\* (deletes only files)*

* rm -r path_to_dir/\* (deletes both files and directories)*

-   Creating symbolic link

ln -s source symbolic_link

-   Finding (?)

find /path/to/dir -newermt \"date\"

-   Finding any file by filename (starting from root)

sudo find / -name "xelatex"

-   To copy contents of a file to clipboard

cat source.c \| xclip -selection c

-   To find (or locate) a file and open it using xdg-open

find \~/ -iname \"linux_commands.odt\" \| xargs xdg-open

-   -   <https://stackoverflow.com/questions/17124288/xdg-open-doesnt-work-when-another-commands-output-is-piped-to-it>

-   To search for a word in a file (starting from any directory)

-   Piping with vs. without xargs

    -   <https://stackoverflow.com/questions/35589179/when-to-use-xargs-when-piping/35590714>
    -   Pipe with xargs =\> argument to next command; pipe without xargs
        =\> content to next command (See example with ls and grep)

-   Searching for hypheanted text in man

man grep \| grep \-- -l

(grep \[options\] pattern \[files\])

-   To read the first x lines of a file

    -   head -n x \[FILE\]

-   To read selected sections of a file

    -   cut -d ' ' -f 4

        -   The above command when executed separates elements based on
            ' ' (space delimiter) and reads the 4^th^ word

-   Sorting lines of text

    -   sort -V \[FILE\]

-   Get directory size

    -   sudo du -sh /dirname

-   Get image dimensions (JPEG)

    -   file myimage.jpeg \| grep -Eo \"\[\[:digit:\]\]+ \*x
        \*\[\[:digit:\]\]+\"
    -   [*Find Out Image Dimensions from the Linux Terminal \| Baeldung
        on Linux*](https://www.baeldung.com/linux/image-dimensions)

-   Mount external drive in WSL

    -   sudo mount -t drvfs H: /mnt/h
    -   sudo umount /mnt/h
    -   [*Mount and Access Hard Drives in Windows Subsystem for Linux
        (WSL) - Linux
        Nightly*](https://linuxnightly.com/mount-and-access-hard-drives-in-windows-subsystem-for-linux-wsl/)

-   Curl

    -    curl -o output_path/output.html URL

        -   -o vs. -O

    -   Use -L flag if URL involves re-direction

    -   Use -I to query response headers

    -   

-   **Tip**: Use ANSI C Quoting with echo: echo\$'Hello\\nWorld!!!'

-   Passing strings to commands that expect file

    -   <https://unix.stackexchange.com/questions/505828/how-to-pass-a-string-to-a-command-that-expects-a-file>

-   Graceful exit

    -   <https://gist.github.com/mrbar42/529cf0db529c0408ba1ef414653becdd>

-   Suppress printing -- use /dev/null

    -   echo 'This doesn't print' \> /dev/null
    -   Redirect error messages: cat -INCORRECT-OPTION 2\> /dev/null
    -   Redirect both stdout and stderr: command \> /dev/null 2&1
    -   <https://www.digitalocean.com/community/tutorials/dev-null-in-linux>

-   Permissions
    - `id -u` gives the current user's id
    - `id -un` gives the current user's name
    - `id -g` gives the current user's current group id
    - `id -G` lists all groups
    - `cat /etc/group` gives a more detailed view into the various groups and the list of users in each group.
       - each line is of the form `group_name:passwd:id:users`
       - refer [here](https://www.cyberciti.biz/faq/understanding-etcgroup-file/) for more details
    - `groupdel GROUPNAME` to delete a group
    - `useradd` to add a new user

-   Docx to markdown

    -   Use pandoc

        -   `pandoc -f docx -t markdown foo.docx -o foo.markdown`

    -   Installing pandoc

        -   Download pandoc package

        -   Untar and follow instructions in the 'INSTALL' file
            -   [Install ghc](https://www.haskell.org/ghc/distribution_packages.html)
        
        OR
        -   `sudo dpkg -i /path/to/package.deb` 

-   Installing OpenJRE

*sudo apt-get install default-jre*

*java -jre filename.jar*

-   **Installing JDK (Java Developer Kit)**

*sudo apt install default-jdk*

*javac --version*

-   **Changing versions of java and javac**

*sudo update-alternatives \--config java*

*sudo update-alternatives \--config javac*

[**https://dev.to/harsvnc/how-to-change-your-java-and-javac-version-on-ubuntu-linux-1omj**](https://dev.to/harsvnc/how-to-change-your-java-and-javac-version-on-ubuntu-linux-1omj)

-   **Using external libraries in Java**

*javac -cp \<external_lib_path\> Filename.java*

*java -cp \<external_lib_path\>:. ClassName*

[**https://stackoverflow.com/questions/17805997/working-with-and-importing-external-libraries-frameworks-in-java**](https://stackoverflow.com/questions/17805997/working-with-and-importing-external-libraries-frameworks-in-java)

[**https://stackoverflow.com/questions/2096283/including-jars-in-classpath-on-commandline-javac-or-apt**](https://stackoverflow.com/questions/2096283/including-jars-in-classpath-on-commandline-javac-or-apt)

-   **Using JDBC**

    -   **Install MySql Connector**
    -   [**https://help.ubuntu.com/community/JDBCAndMySQL**](https://help.ubuntu.com/community/JDBCAndMySQL)

-   **Eclipse**

    -   **\"Editor does not contain a main type" --
        **[**https://stackoverflow.com/questions/24117713/editor-does-not-contain-a-main-type-in-eclipse**](https://stackoverflow.com/questions/24117713/editor-does-not-contain-a-main-type-in-eclipse)

    -   [**https://stackoverflow.com/questions/50321602/in-eclipse-what-is-the-difference-between-modulepath-and-classpath**](https://stackoverflow.com/questions/50321602/in-eclipse-what-is-the-difference-between-modulepath-and-classpath)

    -   **Creating a Java EE project --
        **[**https://stackoverflow.com/questions/4747518/how-to-add-java-ee-perspective-to-eclipse**](https://stackoverflow.com/questions/4747518/how-to-add-java-ee-perspective-to-eclipse)

    -   **Add new server to an existing Eclipse project**

        -   **On the \`Servers\` tab in the console, right-click and
            create a new server**

-   Installing Apache Tomcat

    -   <https://youtu.be/wDS4QgehTSI>
    -   To start/ shutdown Tomcat from cmd line:
        */usr/local/apache\*/bin/startup.sh* (or *shutdown.sh*)

-   Installing apache2, php7 and enabling extensions for drupal

*(*[*https://askubuntu.com/questions/451708/php-script-not-executing-on-apache-server*](https://askubuntu.com/questions/451708/php-script-not-executing-on-apache-server)*)*

sudo apt-get install apache2 php7.4 libapache2-mod-php7.4

a2query -m php7.4

sudo a2enmod php7.4

sudo service apache2 restart

*(*[*https://stackoverflow.com/questions/24351260/how-to-check-which-php-extensions-have-been-enabled-disabled-in-ubuntu-linux-12*](https://stackoverflow.com/questions/24351260/how-to-check-which-php-extensions-have-been-enabled-disabled-in-ubuntu-linux-12)*)*

sudo apt-get install php7.4-gd

sudo apt-get install php7.4-dom

sudo apt-get install php-db php-sql

sudo apt-get install php-mysql

sudo service apache2 restart

*(*[*https://www.youtube.com/watch?v=Lhu6co9hm3k*](https://www.youtube.com/watch?v=Lhu6co9hm3k)*)*

sudo chown -R gokulakrishnan /var/www/html/d9

sudo chown -R www-data: /var/www/html/d9

-   Enabling Clean URLs -
    <https://drupal.stackexchange.com/questions/54563/how-can-i-enable-clean-urls>

-   Database Configuration -
    <https://askubuntu.com/questions/766900/mysql-doesnt-ask-for-root-password-when-installing>
    (answer by DimiDak)

-   **Permissions**

    -   *sudo chown -R \<user-name\> \<directory-name\>*
    -   *sudo chmod -R -f 777
        *[*https://superuser.com/questions/451475/chmod-doesnt-work*](https://superuser.com/questions/451475/chmod-doesnt-work)

-   Linux Mint installation
    -   `sudo apt update`
    -   Apache: `sudo apt install apache2`
    -   PHP: 
        -   Add `ppa:ondrej/php` repository: `sudo apt-add-repository ppa:ondrej/php` 
        -   `apt-cache policy php7.4`
        -   `sudo apt install php7.4=[]`, where `[]` is one of the entries in the `Version table` section of the previous command's output
        -   `sudo apt install php7.4-mysqli`
        -   Refer [1](https://stackoverflow.com/questions/40801460/how-to-install-an-older-version-of-php-using-apt-get), [2](https://askubuntu.com/questions/1424971/how-to-upgrade-php-to-7-4-30)
    -   MySQL
        -   `sudo apt install mysql-server-8.0=[]`
    -   Setting up a Codeigniter project
        -   Extract the project into `/var/www/html/` (Let's say the name of the project is `myProject`)
        -   Set up permissions
            -   Refer [here](https://serverfault.com/questions/200650/what-is-sudo-chown-r-www-datawww-data)
        -   Change base URL
        -   Configure Database
        -   Configure Apache
            -   `vim /etc/apache2/sites-available/myProject.conf`
            ```
            <VirtualHost *:80>
            ServerName 127.0.0.1
            ServerAlias 127.0.0.1
            DocumentRoot /var/www/html/myProject
            <Directory /var/www/html/myProject>
                  Allowoverride All
            </Directory>
            </VirtualHost>
            ```
        -   To run the project (application), hit the base URL in the browser
        -   References [1](https://www.howtoforge.com/tutorial/ubuntu-codeigniter/), [2](https://computingforgeeks.com/install-codeigniter-php-framework-on-ubuntu/)

-   Starting MATLAB

export MESA_LOADER_DRIVER_OVERRIDE=i965; matlab

-   Starting MySQL

sudo mysql -u root -p

-   Installing phpmyadmin-

    -   [*https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-20-04*](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-20-04)
    -   [*https://stackoverflow.com/questions/26891721/phpmyadmin-not-found-after-install-on-apache-ubuntu*](https://stackoverflow.com/questions/26891721/phpmyadmin-not-found-after-install-on-apache-ubuntu)

-   How to get 'Edit as Administrator' in Nautilus

sudo apt install nautilus-admin

sudo nautilus-q

-   Installing composer

<https://phoenixnap.com/kb/how-to-install-composer-ubuntu-18-04>

-   To use VM

sudo modprobe vboxdrv

-   Using apt-get (Ipv6; Connection error)

sudo apt-get -o Acquire::ForceIPv4=true \<rest of the command\>

<https://stackoverflow.com/questions/50856080/0-connecting-to-in-archive-ubuntu-com-takes-too-long-time/50856642>

-   Viewing audio devices

aplay -l

arecord -L

-   Recording both input and output sounds in recordmydesktop

    -   Method 1: Stereo Mix

        -   [https://superuser.com/questions/769249/how-to-record-both-input-and-output-audio-](https://superuser.com/questions/769249/how-to-record-both-input-and-output-audio-simultaneously)[simultaneously](https://superuser.com/questions/769249/how-to-record-both-input-and-output-audio-simultaneously)
            (OR)
        -   <https://askubuntu.com/questions/437098/sterio-mix-in-ubuntu-13-10>

pactl load-module module-loopback (pactl =\> pulse audio control)

-   -   -   <https://askubuntu.com/questions/355082/pulseaudio-loopback-unload-audio-output-devices>
            (unloading the loopback module)

*pactl unload-module 24*

-   -   Method 2: JACK (JACK Audio Connection Kit) audio server

        -   <https://askubuntu.com/questions/63363/how-to-use-two-sound-sources-while-using-recordmydesktop>

        -   recordmydesktop CLI bugs

            -   <https://arief-jr.blogspot.com/2016/01/running-recordmydesktop-with-command.html>
            -   <https://bugs.launchpad.net/ubuntu/+source/recordmydesktop/+bug/621188>
            -   <https://github.com/Enselic/recordmydesktop/tree/v0.4.0>

-   -   Reply to comment:
        <https://unix.stackexchange.com/questions/3490/how-can-i-record-the-sound-output-with-gtk-recordmydesktop>

-   Indents in LibreOffice Writer (keyboard shortcuts)

<https://askubuntu.com/questions/880369/how-to-increase-decrease-indentation-in-libreoffice>

-   Installing packages

    -   sudo apt install package_name
    -   If package is local, append the path to the package_name

-   Deleting packages

    -   sudo apt remove package_name

-   Checking if a package exists

    -   dpkg -l \<package-name\>

-   Creating .deb packages

    -   <https://youtu.be/ep88vVfzDAo>
    -   <https://blog.packagecloud.io/how-to-build-debian-packages-for-simple-shell-scripts/>
    
-   Repositories for `apt` 
    -   `/etc/apt/sources.list.d`

-   Converting files from one format to another

    -   *libreoffice \--headless \--invisible \--convert-to pdf \*.ppt*

<https://askubuntu.com/questions/11130/how-can-i-convert-a-ppt-to-a-pdf-from-the-command-line>

-   Checking versions in Shell Script

    -   <https://unix.stackexchange.com/questions/285924/how-to-compare-a-programs-version-in-a-shell-script>

-   Bluetooth connectivity

pactl load-module module-bluetooth-discover

<https://askubuntu.com/questions/801404/bluetooth-connection-failed-blueman-bluez-errors-dbusfailederror-protocol-no>

-   Creating symbolic links

ln -s \<dir_name\> \~/\<symlink_name\>

ln -l \~/\<symlink_name\> (for verification)

<https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/>

-   C-library man pages

*sudo apt-get install glibc-doc*

-   Keyboard shortcuts to go to -

    -   Start of command: Ctrl + A
    -   End of command: Ctrl + E

-   To shut down unresponsive programs/ "restart"

    -   Alt + F2; type 'xkill'; place 'X' on window to be closed
    -   Alt + F2; type 'r'

-   TTY

    -   To open TTY - Ctrl + Alt + F3 (upto F6)
    -   To close TTY -- Ctrl + Alt + F2 (to return to GUI)

-   Installing R - <https://cran.r-project.org/>

-   404 Error (PPA) --
    <https://askubuntu.com/questions/65911/how-can-i-fix-a-404-error-when-using-a-ppa-or-updating-my-package-lists>

(Go to Software Manager \> Other Software and uncheck)

-   Unzipping and installing .tar.gz --
    <https://askubuntu.com/questions/191390/how-to-use-sudo-command-to-install-tar-gz>

-   Target Packages configured multiple times --

    -   <https://askubuntu.com/questions/760896/how-can-i-fix-apt-error-w-target-packages-is-configured-multiple-times>
    -   <https://itsfoss.com/fixing-target-packages-configured-multiple-times/>

-   Redirection (input and output)

./a.out \< inputFile.txt \> outputFile.txt (OR)

freopen(\"input.txt\", \"r\", stdin);

freopen("output.txt", "w", stdout);

-   Installing Node.js

    -   Use curl
    -   use npm link to link with \@angular/cli

-   Killing a process running on a port

    -   sudo kill -9 \$(sudo lsof -t -i:PORT_NUM)

(-9 is for force kill)

-   -   <https://stackoverflow.com/questions/9346211/how-to-kill-a-process-on-a-port-on-ubuntu>

-   Viewing processes running on ports

    -   lsof -t -itcp:PORT_NUM
    -   <https://askubuntu.com/questions/227161/how-can-we-find-which-process-is-using-a-particular-port>

-   Conda

    -   `anaconda-navigator`
    -   `jupyter-notebook` (to access Jupyter Notebook directly)
    -   `conda env --name myvenv python=3.x`
    -   `conda env list`
    -   `conda config --set auto_activate_base false` - to prevent default activation of base environment


-   Adding chromedriver to PATH

    -   <https://askubuntu.com/questions/1235957/how-to-add-chromedriver-to-path-in-ubuntu>

-   Hamachi installation

    -   <https://help.ubuntu.com/community/Hamachi>

-   Check SSH status

    -   sudo systemctl status ssh

-   Enabling KVM for Android Studio

    -   <https://help.ubuntu.com/community/KVM/Installation>

        -   <https://askubuntu.com/questions/1089753/e-package-libvirt-bin-has-no-installation-candidate>
        -   <https://askubuntu.com/questions/1056635/error-no-candidate-version-found-for-kvm>

    -   <https://developer.android.com/studio/run/emulator-acceleration#dependencies-gpu>

        -   <https://stackoverflow.com/questions/47630630/android-sdk-ubuntu-default-path>
        -   <https://askubuntu.com/questions/885658/android-sdk-repositories-cfg-could-not-be-loaded>
        -   <https://stackoverflow.com/questions/10269274/i-get-command-not-found-when-i-try-to-run-android-emulator-on-mac-os-x>
        -   <https://stackoverflow.com/questions/26483370/android-emulator-error-message-panic-missing-emulator-engine-program-for-x86>

-   Docker

    -   <https://stackoverflow.com/questions/64221861/an-error-failed-to-solve-with-frontend-dockerfile-v0>
    -   Running a container in non-root mode
        ```bash
        docker container run --rm \
        -v ${PWD}:/path/in/container \
        -w /path/in/container \
        -u $(id -u):$(id -g) \
        tensorflow/tensorflow
        ```
        Source [here](https://jtreminio.com/blog/running-docker-containers-as-current-host-user/)

-   Start MongoDB

    -   sudo systemctl enable mongod.service
    -   <https://askubuntu.com/questions/61503/how-to-start-mongodb-server-on-system-start>

-   Removing a package using snap

    -   sudo snap remove \<package-name\>

-   Compressing images using imagemagick

    -   <https://stackoverflow.com/questions/7261855/recommendation-for-compressing-jpg-files-with-imagemagick>

Other questions and stuff to look into

-   MATLAB versions
-   When to work as root?
-   .localhost in Firefox
-   usr, etc files -- what do they hold?
-   Chown command
-   Enable password for MySql

R

-   assignemt \<-
-   3 datatypes -- numeric, character, logical(T, F, TRUE, FALSE)
-   case-sensitive
-   use the function c(\...) for vector
-   use as.factor(\...) to categorize data
-   use list(\...) to create a list
-   

Passwords

-   MySQL: username- root; password: <CS@iitm91>
-   Drupal: username- gokullan; password: <CS@iitm91>
