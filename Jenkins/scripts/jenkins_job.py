#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import logging
logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.DEBUG)
basic_config_xml = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.plugins.git.GitSCM" plugin="git@4.0.0">
    <configVersion>2</configVersion>
    <userRemoteConfigs>
      <hudson.plugins.git.UserRemoteConfig>
        <url>{git_url}</url>
      </hudson.plugins.git.UserRemoteConfig>
    </userRemoteConfigs>
    <branches>
      <hudson.plugins.git.BranchSpec>
        <name>{branch_specifier}</name>
      </hudson.plugins.git.BranchSpec>
    </branches>
    <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
    <submoduleCfg class="list"/>
    <extensions/>
  </scm>
  <assignedNode>{assign_node}</assignedNode>
  <canRoam>false</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers>
    <com.fortify.plugin.jenkins.FortifyPlugin plugin="fortify@19.1.30-ENVISION">
      <analysisRunType>
        <value>local</value>
        <projectScanType class="com.fortify.plugin.jenkins.steps.types.JavaScanType">
          <javaVersion>1.8</javaVersion>
          <javaClasspath></javaClasspath>
          <javaSrcFiles>.</javaSrcFiles>
          <javaAddOptions>-64 -encoding UTF-8</javaAddOptions>
        </projectScanType>
        <buildId>{app_name}</buildId>
        <scanFile>{app_name}-{short_branch_specifier}.fpr</scanFile>
        <maxHeap></maxHeap>
        <addJVMOptions></addJVMOptions>
        <translationExcludeList>**/test/*</translationExcludeList>
        <translationDebug>false</translationDebug>
        <translationVerbose>false</translationVerbose>
        <translationLogFile></translationLogFile>
        <runScan>
          <customRulepacks></customRulepacks>
          <additionalOptions>-64 -encoding UTF-8</additionalOptions>
          <debug>false</debug>
          <verbose>false</verbose>
          <logFile></logFile>
        </runScan>
        <uploadSSC>
          <appName>{app_name}</appName>
          <appVersion>{app_version}</appVersion>
          <filterSet></filterSet>
          <searchCondition></searchCondition>
          <pollingInterval></pollingInterval>
        </uploadSSC>
      </analysisRunType>
    </com.fortify.plugin.jenkins.FortifyPlugin>
  </publishers>
  <buildWrappers/>
</project>
"""

jenkins_url = 'http://192.168.198.128:8080'
auth = ('admin', '117241e439c1e1b3d3a6e2349aeec2d0ad')
headers = {"Content-Type": "application/xml"}


def func_modify_job(job_name, git_url, branch_specifier, app_name, short_branch_specifier="", app_version="1.0", assign_node="windows-fortify"):
    job_config_url = jenkins_url + "/job/{}/config.xml"
    job_config_url = job_config_url.format(job_name)
    r = requests.get(job_config_url, auth=auth)
    payload = basic_config_xml.format(git_url=git_url, branch_specifier=branch_specifier, app_name=app_name,
                                      short_branch_specifier=short_branch_specifier, app_version=app_version, assign_node=assign_node)
    logging.debug(payload)
    if r.status_code != 200:
        job_create_url = jenkins_url + "/createItem?name={}"
        job_create_url = job_create_url.format(job_name)
        r = requests.post(job_create_url, data=payload,
                          auth=auth, headers=headers)
        logging.debug(r.text)
    else:
        r = requests.post(job_config_url, data=payload,
                          auth=auth, headers=headers)
        logging.debug(r.text)
    if r.status_code == 200:
        logger.info("Jenkins job {} created/updated succeed".format(job_name))
    else:
        logger.info("Jenkins job {} created/updated failed".format(job_name))


def func_start_job(job_name):
    job_build_url = jenkins_url + "/job/{}/build"
    job_build_url = job_build_url.format(job_name)
    r = requests.post(job_build_url, auth=auth)
    logging.debug(r.text)
    if r.status_code == 201:
        logger.info("Jenkins job {} start succeed".format(job_name))
    else:
        logger.info("Jenkins job {} start failed".format(job_name))


if __name__ == '__main__':
    func_modify_job(job_name="test2", git_url="https://github.com/qweraqq/SpringBootSecurityDemo.git",
                    branch_specifier="*/master", app_name="test", short_branch_specifier="master1")

    func_start_job("test2")
