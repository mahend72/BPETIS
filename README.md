# Blockchain-Enabled Private Threat Intelligence Sharing (BEPTIS) Framework

## Overview

Blockchain-Enabled Private Threat Intelligence Sharing (BEPTIS) framework is a tool, that aims to securely share prioritized indicators of compromise (IOCs) related to cyber threats within the Additive Manufacturing (AM) industry without revealing the underlying threat details.

## Research Problem

Sharing threat intelligence among competing organizations can be challenging due to concerns about privacy and competitiveness. Existing systems may lack adequate security, transparency, or efficient data analysis capabilities. This research addresses this problem by developing a dedicated framework for AM that:

- Enables secure and tamper-resistant sharing of prioritized IOCs.
- Preserves the privacy of the underlying threat information.
- Facilitates collaborative threat analysis and risk assessment within the AM community.

## Motivation

Cyber threats pose a significant risk to the AM industry, with potential consequences like disruptions in production, theft of intellectual property, and reputational damage. Effective information sharing is crucial for combating these threats, but concerns about data privacy can hinder collaboration. The BEPTIS framework aims to overcome this obstacle by providing a secure and confidential platform for AM organizations to share and analyze threat intelligence.

## Proposed BEPTIS Framework

The BEPTIS framework offers a unique combination of technologies for secure and private threat intelligence sharing:

- **Structured Threat Information eXpression (STIX):** Standardizes threat data format for seamless exchange between systems.
- **Trusted Automated eXchange of Indicator Information (TAXII):** Facilitates secure communication and authorization for threat data exchange.
- **Hyperledger Fabric:** Provides a private blockchain network for secure and tamper-proof storage of metadata and hash values related to IOCs.
- **Homomorphic encryption:** Enables computations on encrypted IOC data without revealing the underlying threat information.
- **Publish-subscribe subsystem:** Enables efficient and secure messaging for timely threat information dissemination among AM organizations.

## Key Findings

The report highlights several key findings regarding the BEPTIS framework:

- **Enhanced Data Integrity:** The blockchain ensures accurate and verifiable records of IOCs, simplifying access control and limiting unauthorized access.
- **Preserved Privacy:** Homomorphic encryption allows analyses and prioritization of IOCs without revealing sensitive threat details.
- **Efficient Threat Sharing:** The publish-subscribe system facilitates rapid updates and information dissemination among AM organizations.
- **Performance Trade-offs:** Integrating Hyperledger Fabric introduces slight delays but improves CPU utilization, requiring careful consideration of resource constraints.

## Summary

The BEPTIS framework presents a promising approach for secure and private threat intelligence sharing within the AM industry. Its combination of standardized data formats, secure communication protocols, and privacy-preserving encryption techniques offer a valuable tool for enhancing collaboration and resilience against cyber threats. Further research and development can optimize performance and functionalities to fully realize the potential of this framework in strengthening AM cybersecurity.
