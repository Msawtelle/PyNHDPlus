import os
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError


base_url = 'https://s3.amazonaws.com/nhdplus/NHDPlusV21/Data/NHDPlus'

# dictionary of drainage areas
DD = {'AMERICAN SAMOA': 'PI',
      'ARK-RED-WHITE': 'MS',
      'CALIFORNIA': 'CA',
      'GREAT BASIN': 'GB',
      'GREAT LAKES': 'GL',
      'GUAM': 'PI',
      'HAWAII': 'HI',
      'LOWER COLORADO': 'CO',
      'LOWER MISSISSIPPI': 'MS',
      'LOWER MISSOURI': 'MS',
      'MID-ATLANTIC': 'MA',
      'NORTHEAST': 'NE',
      'NORTHERN MARIANA ISLANDS': 'PI',
      'OHIO': 'MS',
      'PACIFIC NORTHWEST': 'PN',
      'PUERTO RICO/U.S. VIRGIN ISLANDS': 'CI',
      'RIO GRANDE': 'RG',
      'SOURIS-RED-RAINY': 'SR',
      'SOUTH ATLANTIC NORTH': 'SA',
      'SOUTH ATLANTIC SOUTH': 'SA',
      'SOUTH ATLANTIC WEST': 'SA',
      'TENNESSEE': 'MS',
      'TEXAS': 'TX',
      'UPPER COLORADO': 'CO',
      'UPPER MISSISSIPPI': 'MS',
      'UPPER MISSOURI': 'MS',
      }
# VPU in each drainage area
DA_to_VPU = {'PN': ['17'],
             'CA': ['18'],
             'GB': ['16'],
             'CO': ['14', '15'],
             'MS': ['05', '06', '07', '08', '10U', '10L', '11'],
             'TX': ['12'],
             'RG': ['13'],
             'SR': ['09'],
             'SA': ['03N', '03S', '03W'],
             'GL': ['04'],
             'MA': ['02'],
             'NE': ['01'],
             'PI': ['22AS', '22GU', '22MP'],
             'HI': ['20'],
             'CI': ['21'],
             }



VPU_to_DA = {'01': 'NE',
             '02': 'MA',
             '03N': 'SA',
             '03S': 'SA',
             '03W': 'SA',
             '04': 'GL',
             '05': 'MS',
             '06': 'MS',
             '07': 'MS',
             '08': 'MS',
             '09': 'SR',
             '10U': 'MS',
             '10L': 'MS',
             '11': 'MS',
             '12': 'TX',
             '13': 'RG',
             '14': 'CO',
             '15': 'CO',
             '16': 'GB',
             '17': 'PN',
             '18': 'CA',
             '20': 'HI',
             '21': 'CI',
             '22AS': 'PI',
             '22GU': 'PI',
             '22MP': 'PI',
             }

# name of each VPU
VPU_names = {'01': 'NORTHEAST',
             '02': 'MID-ATLANTIC',
             '03N': 'SOUTH ATLANTIC NORTH',
             '03S': 'SOUTH ATLANTIC SOUTH',
             '03W': 'SOUTH ATLANTIC WEST',
             '04': 'GREAT LAKES',
             '05': 'OHIO',
             '06': 'TENNESSEE',
             '07': 'UPPER MISSISSIPPI',
             '08': 'LOWER MISSISSIPPI',
             '09': 'SOURIS-RED-RAINY',
             '10U': 'UPPER MISSOURI',
             '10L': 'LOWER MISSOURI',
             '11': 'ARK-RED-WHITE',
             '12': 'TEXAS',
             '13': 'RIO GRANDE',
             '14': 'UPPER COLORADO',
             '15': 'LOWER COLORADO',
             '16': 'GREAT BASIN',
             '17': 'PACIFIC NORTHWEST',
             '18': 'CALIFORNIA',
             '20': 'HAWAII',
             '21': 'PUERTO RICO/U.S. VIRGIN ISLANDS',
             '22AS': 'AMERICAN SAMOA',
             '22GU': 'GUAM',
             '22MP': 'NORTHERN MARIANA ISLANDS',

             }
# RPU of each drainage area
VPU_to_RPU = {'01': ['01A'],
              '02': ['02A', '02B'],
              '03N': ['03A', '03B'],
              '03S': ['03C', '03D'],
              '03W': ['03E', '03F'],
              '04': ['04A', '04B', '04C', '04D'],
              '05': ['05A', '05B', '05C', '05D'],
              '06': ['06A'],
              '07': ['07A', '07B', '07C'],
              '08': ['08A', '08B', '03G'],
              '09': ['09A'],
              '10U': ['10E', '10F', '10G', '10H', '10I'],
              '10L': ['10A', '10B', '10C', '10D'],
              '11': ['11A', '11B', '11C', '11D'],
              '12': ['12A', '12B', '12C', '12D'],
              '13': ['13A', '13B', '13C', '13D'],
              '14': ['14A', '14B'],
              '15': ['15A', '15B'],
              '16': ['16A', '16B'],
              '17': ['17A', '17B', '17C', '17D'],
              '18': ['18A', '18B', '18C'],
              '20': ['20A', '20B', '20C', '20D', '20E', '20F', '20G', '20H'],
              '21': ['21A', '21B', '21C'],
              '22AS': ['22C'],
              '22GU': ['22A'],
              '22MP': ['22B'],
              }


RPU_to_VPU = {'01a': '01',
              '02a': '02',
              '02b': '02',
              '03a': '03N',
              '03b': '03N',
              '03c': '03S',
              '03d': '03S',
              '03e': '03W',
              '03f': '03W',
              '03g': '08',
              '04a': '04',
              '04b': '04',
              '04c': '04',
              '04d': '04',
              '05a': '05',
              '05b': '05',
              '05c': '05',
              '05d': '05',
              '06a': '06',
              '07a': '07',
              '07b': '07',
              '07c': '07',
              '08a': '08',
              '08b': '08',
              '09a': '09',
              '10a': '10L',
              '10b': '10L',
              '10c': '10L',
              '10d': '10L',
              '10e': '10U',
              '10f': '10U',
              '10g': '10U',
              '10h': '10U',
              '10i': '10U',
              '11a': '11',
              '11b': '11',
              '11c': '11',
              '11d': '11',
              '12a': '12',
              '12b': '12',
              '12c': '12',
              '12d': '12',
              '13a': '13',
              '13b': '13',
              '13c': '13',
              '13d': '13',
              '14a': '14',
              '14b': '14',
              '15a': '15',
              '15b': '15',
              '16a': '16',
              '16b': '16',
              '17a': '17',
              '17b': '17',
              '17c': '17',
              '17d': '17',
              '18a': '18',
              '18b': '18',
              '18c': '18',
              '20a': '20',
              '20b': '20',
              '20c': '20',
              '20d': '20',
              '20e': '20',
              '20f': '20',
              '20g': '20',
              '20h': '20',
              '21a': '21',
              '21b': '21',
              '21c': '21',
              '22a': '22GU',
              '22b': '22MP',
              '22c': '22AS',
            }



# different types of rpu files on the website
RPU_Files = ['CatSeed', 'FdrFac', 'FdrNull', 'FilledAreas', 'HydroDem', 'NEDSnapshot','Hydrodem','Catseed']
VPU_Files = ['EROMExtension', 'NHDPlusAttributes', 'NHDPlusBurnComponents', 'NHDPlusCatchment', 'NHDSnapshot',
             'VPUAttributeExtension', 'VogelExtension', 'WBDSnapshot', 'NHDSnapshotFGDB',]

All_Files = ['CATSEED', 'FDRFAC', 'FDRNULL', 'FILLEDAREAS', 'HYDRODEM', 'NEDSNAPSHOT', 'EROMEXTENSION',
             'NHDPLUSATTRIBUTES', 'NHDPLUSBURNCOMPONENTS','NHDPLUSCATCHMENT', 'NHDSNAPSHOT', 'VPUATTRIBUTEEXTENSION',
             'VOGELEXTENSION', 'WBDSNAPSHOT', 'NHDSNAPSHOTFGDB']


#EPA's website is poorly organized this list makes navigating it a bit easier

problematic_vpu_list = ['03N', '03S', '03W','05', '06', '07', '08',
                        '10U', '14', '15', '10L', '11','22AS', '22GU', '22MP']

link_file = 'link.txt'

known_exceptions = {(base_url+'GL/NHDPlusV21_GL_04_NHDPlusCatchment'):(base_url+'GL/NHDPlusV21_GL_04_NHDPlusCatchments'),
                    (base_url+'CO/NHDPlus15/NHDPlusV21_CO_15_VogelExtension'):(base_url+'CO/NHDPlus15/NHDPlusV21_CO_15_VogelEXtension')}




def gather_rpu_links(max_version=15, rpu_input=None, filename_input=None):
    '''
    A function to gather the working rpu links for the metadata text file

    max_version takes the highest know version of the files in the NHDPLUS Dataset

    the two optional arguments facilitate getting one link in the case that the metadata file is not up to data
    rpu_input takes a specific rpu region to gather one link
    filename_input takes a specific rpu filename to gather one link

    '''

    working_urls = []


    if rpu_input is None and filename_input is None:
        for rpu in sorted(RPU_to_VPU.keys()):

            vpu = RPU_to_VPU[rpu]
            DA = VPU_to_DA[vpu]

            for filename in RPU_Files:

                if vpu in problematic_vpu_list:
                    url = '{0}{1}/NHDPlus{2}/NHDPlusV21_{1}_{2}_{3}_{4}'.format(base_url, DA, vpu, rpu, filename)

                    i = 1
                    while i < max_version+1:

                        final_url = '{}_{:02d}.7z'.format(url,i)

                        try:
                            req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                            response = urlopen(req)
                            working_urls.append(final_url)
                            print('FOUND ' + final_url)
                            break
                        except HTTPError or URLError:
                            pass
                        i += 1

                else:
                    url = '{0}{1}/NHDPlusV21_{1}_{2}_{3}_{4}'.format(base_url, DA, vpu, rpu, filename)

                    i = 1

                    while i < max_version+1:

                        final_url = '{}_{:02d}.7z'.format(url, i)


                        try:
                            req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                            response = urlopen(req)
                            working_urls.append(final_url)
                            print('FOUND '+ final_url)
                            break
                        except HTTPError or URLError:
                            pass
                        i+= 1

                if i > max_version:
                    print('no link found for ', final_url)
                    pass

        return working_urls

    else:
        vpu = RPU_to_VPU[rpu_input]
        DA = VPU_to_DA[vpu]

        if vpu in problematic_vpu_list:
            url = '{0}{1}/NHDPlus{2}/NHDPlusV21_{1}_{2}_{3}_{4}'.format(base_url, DA, vpu, rpu, filename)

            i = 1
            while i < max_version+1:

                final_url = '{}_{:02d}.7z'.format(url,i)

                try:
                    req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                    response = urlopen(req)
                    working_urls.append(final_url)
                    print('FOUND ' + final_url)
                    break
                except HTTPError or URLError:
                        pass
                i += 1

        else:

            url = '{0}{1}/NHDPlusV21_{1}_{2}_{3}_{4}'.format(base_url, DA, vpu, rpu, filename)

            i = 1

            while i < max_version+1:

                final_url = '{}_{:02d}.7z'.format(url, i)


                try:
                    req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                    response = urlopen(req)
                    working_urls.append(final_url)
                    print('FOUND '+ final_url)
                    break
                except HTTPError or URLError:
                    pass
                i+= 1

        if i > max_version:
            print('no link found for ', final_url)
            pass

        return working_urls


def gather_vpu_links(max_version=15, vpu_input=None, filename_input=None):
    '''
    A function to gather the working vpu links for the metadata text file

    max_version takes the highest known version of the files in the NHDPLUS Dataset

    the two optional arguments facilitate getting one link in the case that the metadata file is not up to data
    vpu_input takes a specific vpu region to gather one link
    filename_input takes a specific vpu filename to gather one link
    '''
    working_urls = []

    if vpu_input is None and filename_input is None:

        for vpu in sorted(VPU_to_DA.keys()):

            DA = VPU_to_DA[vpu]

            for filename in VPU_Files:

                if vpu in problematic_vpu_list:

                    url = '{0}{1}/NHDPlus{2}/NHDPlusV21_{1}_{2}_{3}'.format(base_url,DA,vpu,filename)
                    if url in known_exceptions.keys():
                        url = known_exceptions[url]

                    i = 1
                    while i < max_version+1:

                        final_url = '{}_{:02d}.7z'.format(url,i)

                        try:
                            req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                            response = urlopen(req)
                            working_urls.append(final_url)
                            print('FOUND '+final_url)
                            break
                        except HTTPError or URLError:
                            pass
                        i += 1


                else:

                    url = '{0}{1}/NHDPlusV21_{1}_{2}_{3}'.format(base_url,DA,vpu,filename)
                    if url in known_exceptions.keys():
                        url = known_exceptions[url]
                    i = 1
                    while i < max_version+1:
                        final_url = '{}_{:02d}.7z'.format(url,i)

                        try:
                            req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                            response = urlopen(req)
                            working_urls.append(final_url)
                            print('FOUND '+ final_url)
                            break
                        except HTTPError or URLError:
                            pass
                        i += 1

                if i > max_version:
                    print('no link found for ', final_url)
                    pass

        return working_urls

    else:

        DA = VPU_to_DA[vpu_input]

        if vpu_input in problematic_vpu_list:

            url = '{0}{1}/NHDPlus{2}/NHDPlusV21_{1}_{2}_{3}'.format(base_url,DA,vpu_input,filename_input)
            if url in known_exceptions.keys():
                url = known_exceptions[url]

            i = 1
            while i < max_version+1:

                final_url = '{}_{:02d}.7z'.format(url,i)

                try:
                    req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                    response = urlopen(req)
                    working_urls.append(final_url)
                    print('FOUND '+final_url)
                    break
                except HTTPError or URLError:
                    pass
                i += 1


        else:

            url = '{0}{1}/NHDPlusV21_{1}_{2}_{3}'.format(base_url,DA,vpu_input,filename_input)
            if url in known_exceptions.keys():
                url = known_exceptions[url]
            i = 1
            while i < max_version+1:
                final_url = '{}_{:02d}.7z'.format(url,i)

                try:
                    req = Request(final_url, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                    response = urlopen(req)
                    working_urls.append(final_url)
                    print('FOUND '+ final_url)
                    break
                except HTTPError or URLError:
                    pass
                i += 1

        if i > max_version:
            print('no link found for ', final_url)
            pass

        return working_urls





def get_VPU_File(vpu, filename):

    '''
    A function to return the desired VPU File

    Arguments:
        vpu takes any of the keys in the VPU_to_RPU dictionary
        filename takes any of the values in the VPU_Files list

    '''

    assert vpu in VPU_to_RPU.keys(), 'VPU must be in ' + str(sorted(VPU_to_RPU.keys()))

    assert filename in VPU_Files, 'filename must be one of ' + str(VPU_Files)

    DA = VPU_to_DA[vpu]


    if vpu in problematic_vpu_list:

        url = '{0}{1}/NHDPlus{2}/NHDPlusV21_{1}_{2}_{3}'.format(base_url,DA,vpu,filename)


    else:

        url = '{0}{1}/NHDPlusV21_{1}_{2}_{3}'.format(base_url,DA,vpu,filename)


    with open(link_file) as f:

        verified_links = f.read().splitlines()
    i = 0
    while True:

        if url in verified_links[i]:
            break
        i += 1

        if i > (len(verified_links) - 1) :
            print('link' + ' ' + url +' not found')
            raise 'gather'

    return verified_links[i]



def get_RPU_file(rpu,filename):
    '''
    A function to return the desired RPU file

    Arguments:
        rpu takes any of the keys in the the RPU_to_VPU dictionary
        filename takes any of the value in the RPU_Files list
    '''


    assert rpu in RPU_to_VPU.keys(), 'RPU must be one of the following ' + str(sorted(RPU_to_VPU.keys()))

    assert filename in RPU_Files, 'filename must be one of the following ' + str(sorted(RPU_Files))


    vpu = RPU_to_VPU[rpu]
    DA = VPU_to_DA[vpu]


    if vpu in problematic_vpu_list:

        url = '{0}{1}/NHDPlus{2}/NHDPlusV21_{1}_{2}_{3}_{4}'.format(base_url, DA, vpu, rpu, filename)


    else:

        url = '{0}{1}/NHDPlusV21_{1}_{2}_{3}_{4}'.format(base_url, DA, vpu, rpu, filename)

    with open(link_file) as f:

        verified_links = f.read().splitlines()
    i = 0
    while True:

        if url in verified_links[i]:
            break
        i += 1

        if i > (len(verified_links) - 1) :
            print('link' + ' ' + url +' not found')
            raise

    return verified_links[i]



def verify_links():

    working_links = []

    if os.path.isfile(link_file):

        with open(link_file,'r') as source:
            links = source.read().splitlines()

            for link in links:

                try:
                        req = Request(link, data=None,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'})
                        response = urlopen(req)
                        working_links.append(link)
                        break
                except HTTPError or URLError:
                    print('the following link was broken ' + link)
                    a = link.split('/')[-1]
                    b = a.split('_')

                    if len(b) == 5:
                        working_links.append(gather_vpu_links(vpu_input=b[2], filename_input=b[3]))

                    else:
                        working_links.append(gather_rpu_links(rpu_input=b[3], filename_input=b[4]))

                    break


        with open(link_file,'w') as corrected:

            for items in working_links:

                corrected.write('%s\n' %items)

    else:
        with open(link_file,'w') as destination:
            vpu_links = gather_vpu_links()
            rpu_links = gather_rpu_links()

            for items in vpu_links:
                destination.write('%s\n' % items)

            for items in rpu_links:
                destination.write('%s\n' % items)

verify_links()
