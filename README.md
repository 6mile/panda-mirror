<img width="1110" height="624" alt="panda-mirror-banner-gemini-smaller" src="https://github.com/user-attachments/assets/44f04ad2-6d11-478a-b43d-f5384a6aa4d4" />

# Panda Mirror: How the Chinese CCP Manipulates NPM

This presentation, "Panda Mirror - Canberra BSides," by Paul McCarty, delves into the manipulation of the NPM (Node Package Manager) ecosystem by the Chinese Communist Party (CCP).

## Key Takeaways:

  * **NPM's Scale and Insecurity:** NPM is the world's largest software registry, with millions of packages and thousands of daily updates, yet it was built "before security" and is highly vulnerable to malicious packages.
  * **Global Mirrors and Chinese Anomalies:** There are eight global NPM mirrors. While most mirrors respect package deletion events from the root registry, several Chinese mirrors (r.cnpmjs.org, registry.npmmirror.com, repo.huaweicloud.com, mirrors.cloud.tencent.com, registry.npm.taobao.org) have been modified to store deleted malicious packages.
  * **CCP's Focus on Source Code Weaponization:** The CCP, through regulations like the "Regulations on the Management of Network Product Security Vulnerabilities" (RMSV), is actively focusing on weaponizing software vulnerabilities and has access to internal code repositories. The Chinese NVDB (National Vulnerability Database) does not publish vulnerabilities but shares them with ministry departments for offensive work.
  * **Exploiting the Mirror Discrepancy:** The speaker used the "bug" in the Chinese mirrors (their failure to respect deletion events) to collect NPM malware samples for over a year.
  * **Impact and Solutions:** This intelligence was used to analyze malware, build rules for detection, create a CTI (Cyber Threat Intelligence) portal to track threat actors, and ultimately sold. The presentation highlights the critical need to integrate software supply chain intelligence into enterprise CTI.

This research underscores the significant threat posed by nation-state actors manipulating critical software infrastructure and the importance of understanding and mitigating these risks.

