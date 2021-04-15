## Linux发行版本

### Arch系

- Manjaro

  相对于Arch的激进更新，Manjaro会对AUR再测试，基本迟于Arch两周发布。

  还有自己的pacmac的GUI程序。

### Dedian系

- Ubuntu
- Mint（基于Ubuntu衍生）
- Pop!_OS（基于Ubuntu衍生）
- elementary（基于Ubuntu衍生）
- Ubuntu Kylin（基于Ubuntu衍生）
- Deepin
- Kubuntu（基于Ubuntu衍生）

### Red Hat系

- CentOS

  CentOS（Community Enterprise Operating System）：Red Hat的另一个重要分支，以Red Hat所发布的源代码重建符合GPL许可协议的Linux系统，即将Red Hat Linux源代码的商标（LOGO）及非自由软件部分去除后再编译而成的版本。目前CentOS已被Red Hat公司收购，但仍开源免费。

  稳定才是企业最需要的，所以版本也老

- Fedora

  Red Hat的一个分支，仍遵循GPL协议，可以认为是Red Hat预发布版

  所以不咋稳定，各种小bug不穷。

### openSUSE



## 一些介绍

1. **Arch Linux**

   是一款基于 x86-64架构的发行版本。Arch Linux 采用pacman作为默认的软件包管理器

   Arch Linux 采用[滚动发行](https://zh.wikipedia.org/wiki/滾動發行)模式，即没有所谓的大版本更新，每次常规更新都会将系统和软件保持在最新状态。Arch 发行的系统安装映像也只是简单地包含最新的基本系统组件。

   **优点**

   - Arch Linux是针对特定处理器而优化过的，能够更好地利用[CPU](https://zh.wikipedia.org/wiki/CPU)周期以提高性能。Arch Linux简单的设计让它容易被轻松扩展和配置成为任何想要的系统类型。
   - 通过二进制包管理系统[pacman](https://zh.wikipedia.org/wiki/Pacman)，仅需一个命令就能完成安装、升级等多个操作。同时也附带一个类似[ports](https://zh.wikipedia.org/wiki/Ports)的包构建系统ABS（Arch Build System）。
   - 与[Gentoo](https://zh.wikipedia.org/wiki/Gentoo)类似，不同于其他大部分主流Linux发行版比如[Fedora](https://zh.wikipedia.org/wiki/Fedora)和[Ubuntu](https://zh.wikipedia.org/wiki/Ubuntu)。Arch Linux不采跨版本升级而采用“[滚动更新](https://zh.wikipedia.org/wiki/滚动更新)”，故Arch Linux的软件包时常会维持在开发者的最新版本。

   缺点

   - 安装过程简陋，缺乏直观的错误处理与[图形化安装界面](https://zh.wikipedia.org/wiki/图形用户界面)，需要用户有一定的Linux环境常识才能正确安装使用。
   - 包管理系统pacman在升级过程缺乏对系统核心组件的回溯保护，比如当用户升级到错误的[内核](https://zh.wikipedia.org/wiki/内核)会造成系统无法引导，滚挂也是常有的事。现在好像2周一个更新就没特别大的问题
   - 系统软件缺乏严谨的测试管理机制，稳定性、可靠性不如[Redhat](https://zh.wikipedia.org/wiki/Redhat)、[CentOS](https://zh.wikipedia.org/wiki/CentOS)、[Debian](https://zh.wikipedia.org/wiki/Debian)等发行版[[18\]](https://zh.wikipedia.org/wiki/Arch_Linux#cite_note-18)，难以在企业用户中推广

2. **Ubuntu**

   是以桌面应用为主的[Linux发行版](https://zh.wikipedia.org/wiki/Linux發行版)，基于Debian。Ubuntu有三个正式版本，包括桌面版、[服务器](https://zh.wikipedia.org/wiki/服务器)版及用于[物联网](https://zh.wikipedia.org/wiki/物联网)设备和[机器人](https://zh.wikipedia.org/wiki/机器人)的Core版

   Ubuntu是著名的Linux发行版之一，也是目前最多用户的[Linux](https://zh.wikipedia.org/wiki/Linux)版本。Ubuntu每六个月（即每年的四月与十月）发布一个新版本，长期支持（LTS）版本每两年发布一次。普通版本一般只支持9个月，但LTS版本一般能提供5年的支持。
   
   推荐在Debian系统中管理软件包的标准工具是*apt*工具集。
   
   [dpkg](https://zh.wikipedia.org/wiki/Dpkg)是Debian中软件包管理的低级别基础工具。*dpkg*命令行工具并不知晓软件源的配置，其数据库仅存储已安装在当前系统中的软件包的信息。该工具可以操作本地[.deb](https://zh.wikipedia.org/wiki/Deb)软件包及dpkg数据库内的信息。
   
   ubunt 内部错误
   
3. **Red Hat Linux**

   自从Red Hat 9.0版本发布后，Red Hat公司就不再开发桌面版的Linux发行包，而将全部力量集中在服务器版的开发上，也就是[Red Hat Enterprise Linux](https://zh.wikipedia.org/wiki/Red_Hat_Enterprise_Linux)版。2004年4月30日，Red Hat公司正式停止对Red Hat 9.0版本的支持，标志着Red Hat Linux的正式完结。原本的桌面版Red Hat Linux发行包则与来自民间的Fedora计划合并，成为[Fedora Core](https://zh.wikipedia.org/wiki/Fedora_Core)发行版本

   Red Hat Linux拥有一个图形化的安装程序[Anaconda](https://zh.wikipedia.org/wiki/Anaconda)，目的是为了令新手更容易使用。同时，它有一个内置的[防火墙](https://zh.wikipedia.org/w/index.php?title=防火墙_(计算机)&action=edit&redlink=1)设置工具[Lokkit](https://zh.wikipedia.org/w/index.php?title=Lokkit&action=edit&redlink=1)

4. **openSUSE**

   前身为SUSE Linux和SuSE Linux Professional，是一个[Linux发行版](https://zh.wikipedia.org/wiki/Linux發行版)与项目，由SUSE Linux GmBH与其他公司赞助。openSUSE在全世界被广泛使用，尤其是在德国。它的开发重心是为软件开发者和系统管理者创造适用的开放源代码的工具，并提供易于使用的桌面环境和功能丰富的服务器环境

   **YaST**（**Yet another Setup Tool**，“另一种安装工具”）是 openSUSE 的重要特性之一。它能让系统管理员在集成界面内处理包括磁盘分区、系统安装、网络与防火墙配置、[RPM](https://zh.wikipedia.org/wiki/RPM)软件包管理、在线更新、用户管理等诸多功能。









