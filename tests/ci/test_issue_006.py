# coding: utf-8

# Copyright 2018 www.privaz.io Valletech AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
import pyone.bindings as bindings
from pyone.util import one2dict

utf8Xml = '''<HOST xmlns='http://opennebula.org/XMLSchema'><ID>0</ID><NAME>hv1</NAME><STATE>2</STATE><IM_MAD><![CDATA[kvm]]></IM_MAD><VM_MAD><![CDATA[kvm]]></VM_MAD><LAST_MON_TIME>1520196635</LAST_MON_TIME><CLUSTER_ID>0</CLUSTER_ID><CLUSTER>default</CLUSTER><HOST_SHARE><DISK_USAGE>0</DISK_USAGE><MEM_USAGE>0</MEM_USAGE><CPU_USAGE>0</CPU_USAGE><TOTAL_MEM>1020364</TOTAL_MEM><TOTAL_CPU>100</TOTAL_CPU><MAX_DISK>4976</MAX_DISK><MAX_MEM>1020364</MAX_MEM><MAX_CPU>100</MAX_CPU><FREE_DISK>4684</FREE_DISK><FREE_MEM>934428</FREE_MEM><FREE_CPU>100</FREE_CPU><USED_DISK>21</USED_DISK><USED_MEM>85936</USED_MEM><USED_CPU>0</USED_CPU><RUNNING_VMS>0</RUNNING_VMS><DATASTORES></DATASTORES><PCI_DEVICES></PCI_DEVICES></HOST_SHARE><VMS></VMS><TEMPLATE><ARCH><![CDATA[x86_64]]></ARCH><CPUSPEED><![CDATA[2592]]></CPUSPEED><HOSTNAME><![CDATA[hv1]]></HOSTNAME><HYPERVISOR><![CDATA[kvm]]></HYPERVISOR><IM_MAD><![CDATA[kvm]]></IM_MAD><KVM_CPU_MODELS><![CDATA[486 pentium pentium2 pentium3 pentiumpro coreduo n270 core2duo qemu32 kvm32 cpu64-rhel5 cpu64-rhel6 kvm64 qemu64 Conroe Penryn Nehalem Westmere SandyBridge IvyBridge Haswell-noTSX Haswell Broadwell-noTSX Broadwell Skylake-Client athlon phenom Opteron_G1 Opteron_G2 Opteron_G3 Opteron_G4 Opteron_G5]]></KVM_CPU_MODELS><KVM_MACHINES><![CDATA[pc-i440fx-2.8 pc pc-0.12 pc-i440fx-2.4 pc-1.3 pc-q35-2.7 pc-q35-2.6 xenpv pc-i440fx-1.7 pc-i440fx-1.6 pc-i440fx-2.7 pc-0.11 pc-i440fx-2.3 pc-0.10 pc-1.2 pc-i440fx-2.2 isapc pc-q35-2.5 xenfv pc-0.15 pc-0.14 pc-i440fx-1.5 pc-i440fx-2.6 pc-i440fx-1.4 pc-i440fx-2.5 pc-1.1 pc-i440fx-2.1 pc-q35-2.8 q35 pc-1.0 pc-i440fx-2.0 pc-q35-2.4 pc-0.13]]></KVM_MACHINES><LABELS><![CDATA[HD,LOWPOWER]]></LABELS><MODELNAME><![CDATA[Intel Core Processor (Skylake)]]></MODELNAME><NETRX><![CDATA[0]]></NETRX><NETTX><![CDATA[0]]></NETTX><NOTES><![CDATA[Hostname is: ESPAÑA]]></NOTES><RESERVED_CPU><![CDATA[]]></RESERVED_CPU><RESERVED_MEM><![CDATA[]]></RESERVED_MEM><VERSION><![CDATA[5.4.6]]></VERSION><VM_MAD><![CDATA[kvm]]></VM_MAD></TEMPLATE></HOST>'''


class TestIssue006(unittest.TestCase):
    def test_utf8_names_in_calls(self):
        host = bindings.CreateFromDocument(utf8Xml)
        tdict = one2dict(host.TEMPLATE)
        # note python2 and python3 return different types: str or unicode
        self.assertIn(tdict['TEMPLATE']['NOTES'], ["Hostname is: ESPAÑA",u"Hostname is: ESPAÑA"])