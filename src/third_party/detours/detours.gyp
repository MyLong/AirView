#Copyright(c)2013 The AirView Authors.All rights reserved.
#Use of this source code is governed by a BSD - style license that can be
#found in the LICENSE file.
{
  'targets' :[
               {
                 'target_name' : 'detours',
                 'type' : 'static_library',
                 'includes' :[ 'detours.gypi', ],
                 'conditions' :[
                   [
                     'target_arch == "ia32"',
                     {
                       'defines' :[ 'DETOURS_32BIT=1', 'DETOURS_X86=1', ],
                     }
                   ],
                   [
                     'target_arch == "x64"',
                     {
                       'defines' :[ 'DETOURS_64BIT=1', 'DETOURS_X64=1', ],
                       'configurations' : {
                         'Common_Base' : {
                           'msvs_target_platform' : 'x64',
                         },
                       },
                     }
                   ],
                 ],
                 'sources/' :[
                   [ 'exclude', 'Makefile' ],
                   [ 'exclude', 'detours.gypi' ],
                   [ 'exclude', 'uimports.cpp' ],
                 ],
               },
             ]
}
