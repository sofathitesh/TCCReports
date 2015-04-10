from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from librehatti.settings import TEMPLATE_DIRS
from django.contrib.auth.decorators import login_required
import os
from django.shortcuts import render, render_to_response
from django.shortcuts import RequestContext, HttpResponseRedirect
from django.core.files import File
from librehatti.Test_Reports.models import *
from django.template.loader import render_to_string
from librehatti.voucher.models import VoucherId, Distribution
from librehatti.voucher.models import FinancialSession, CalculateDistribution
from librehatti.voucher.models import VoucherTotal
from librehatti.suspense.models import *
from useraccounts.models import *
from librehatti.catalog.models import *
import os
from subprocess import call
from .forms import Test_Reports

@login_required
def Test_Reports_data(request):
    session = request.GET['session']
    voucher = request.GET['voucher']
    session_id = VoucherId.objects.values('purchased_item_id',\
        'purchase_order_id','purchase_order_of_session').\
    get(session_id=session, voucher_no=voucher)
    purchased_item = PurchasedItem.objects.values('item_id').\
    get(id=session_id['purchased_item_id'])
    product = Product.objects.values('name').\
    get(id=purchased_item['item_id'])    
    purchase_order = PurchaseOrder.objects.values('buyer_id','reference_date').\
    get(id=session_id['purchase_order_id'])
    buyer_id = User.objects.values('first_name','last_name','id').\
    get(id=purchase_order['buyer_id'])
    address_id = Customer.objects.values('address_id').\
    get(user=buyer_id['id'])
    street_address = Address.objects.values('street_address','city').\
    get(id=address_id['address_id'])
    Testing_date = SuspenseClearance.objects.values('test_date').get(id=session)   
    data =buyer_id['first_name']+":"+buyer_id['last_name']+":"+\
    street_address['street_address']+":"+\
    unicode(session_id['purchase_order_of_session'])+":"+\
    Testing_date['test_date']+":"+product['name']+":"+street_address['city']
    if buyer_id['first_name'] is not None:
        return HttpResponse(data)
    else:
        return HttpResponse('fail')

@login_required
def Reports(request):
    data_session = request.session.get('data')
    report_get_id = Test_Reports.objects.values('id','mix').\
    get(Session_id=data_session['Session'], Voucher = data_session['Voucher']) 
    count = 1
    report_content = '' 
    date_format = data_session['Refernce_Date'].split("-")
    date_format_new = date_format[2] + "/" + date_format[1] + "/" +\
    date_format[0]
    date_format_for_test = data_session['Testing_Date'].split("-")
    date_format_new_for_test = date_format_for_test[2] + "/" + \
    date_format_for_test[1] + "/" + date_format_for_test[0]
    filename = "trial_copy.tex"
    texfilename = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/trial.tex'))
    texfilename_copy = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/trial_copy.tex'))
    if request.method == 'POST':
        r = request.POST['header']
    else:
        return render(request,"Test_Reports/index.html",{'r':''})
 
    for des in  Test_Report_Descriptions.objects.filter(report_id_id \
        = report_get_id['id']):

            date_format_for_start = unicode(des.Start_Date).split("-")
            date_format_new_for_start = date_format_for_start[2] + "/" \
            + date_format_for_start[1] + "/" + date_format_for_start[0]
            
            if report_get_id['mix'] == 1:
                report_content += str(count) + "&" + des.Description + \
                "&" + date_format_new_for_start + "&" + des.mix + "&"\
                 + des.Strength + "\\" + "\\" + "\hline"
                if request.POST['header'] == 'yes':
                    texfilename = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), \
                    '../..', 'templates/Test_Reports/trial.tex'))
                    texfilename_copy = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), '../..', \
                    'templates/Test_Reports/trial_copy.tex'))
                    filename = "trial_copy.pdf"
                else:
                    texfilename = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), '../..',  \
                    'templates/Test_Reports/my_latex_tamplate.tex'))
                    texfilename_copy = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), '../..',  \
                    'templates/Test_Reports/my_latex_tamplate_copy.tex'))
                    filename = "my_latex_tamplate_copy.pdf"
                
            else:
                report_content += str(count) + "&" + des.Description + \
                "&" + date_format_new_for_start + "&" + des.Strength +  \
                "\\" + "\\" + "\hline"
                if request.POST['header'] == 'no':                                                    
                    texfilename = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), '../..',  \
                    'templates/Test_Reports/my_tamplate_without_mix.tex'))
                    texfilename_copy = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), '../..', \
                    'templates/Test_Reports/my_tamplate_without_mix_copy.tex'))
                    filename = "my_tamplate_without_mix_copy.pdf"
                else:                                
                    texfilename = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), '../..',  \
                    'templates/Test_Reports/trial_without_mix.tex'))
                    texfilename_copy = os.path.abspath(os.path. \
                    join(os.path.dirname(__file__), '../..',  \
                    'templates/Test_Reports/trial_without_mix_copy.tex'))
                    filename = "trial_without_mix_copy.pdf"

    count += 1               
    if r == 'yes':
        f = open(texfilename,'r+')
        data = f.read()
        f.close()
        fw = open(texfilename_copy,'w+')
        fw.write(data)
        fw.close()
        texfile = os.open(texfilename_copy, os.O_RDWR)
        os.write(texfile, render_to_string(texfilename_copy,  \
            {'address': data_session['Client'].replace('&','\&'),
			'address2': data_session['Address'].replace('&','\&'),
			'address3': data_session['City'].replace('&','\&'),
			'sub': data_session['Subject'].replace('&','\&'),
			'ref_no': data_session['Refernce_no'],
			'ref_date': data_session['Refernce_Date'].replace('-','/'),
			'start_date': data_session['Refernce_Date'].replace('-','/'),
            'table': report_content,    
			'test_date': date_format_new,
			'ref_date': date_format_new_for_test,
			'start_date': date_format_new_for_test,
            'table': report_content,    
			'test_date': date_format_new,
			'ref_date': date_format_new_for_test,
			'start_date': date_format_new_for_test,
            'table': report_content,    
			}))
        os.close(texfile)
        call(['sh',os.path.abspath(os.path. \
            join(os.path.dirname(__file__), '../..', \
            'templates/Test_Reports/shell.sh'))])  
 
    if r == 'no':
        f = open(texfilename,'r+')
        data = f.read()
        f.close()
        fw = open(texfilename_copy,'w+')
        fw.write(data)
        fw.close()
        texfile = os.open(texfilename_copy,os.O_RDWR)
        os.write(texfile, render_to_string(texfilename_copy,\
            {'address': data_session['Client'].replace('&','\&'),
			'address2': data_session['Address'].replace('&','\&'),
			'address3': data_session['City'].replace('&','\&'),
			'sub': data_session['Subject'].replace('&','\&'),
			'ref_no': data_session['Refernce_no'],
			'ref_date': data_session['Refernce_Date'].replace('-','/'),
			'start_date': data_session['Refernce_Date'].replace('-','/'),
            'table': report_content,    
			'test_date': date_format_new,
			'ref_date': date_format_new_for_test,
			'start_date': date_format_new_for_test,
            'table': report_content,    
			'test_date': date_format_new,
			'ref_date': date_format_new_for_test,
			'start_date': date_format_new_for_test,
            'table': report_content,    
			}))
        os.close(texfile)
    call(['sh',os.path.abspath(os.path.join(os.path.dirname(__file__), \
     '../..', 'templates/Test_Reports/shell.sh'))])   
    return render(request,"Test_Reports/index.html",{'r':'/'+filename,\
        'res': request.POST['header']})

@login_required
def Soil_building_report(request):
    data_session = request.session.get('data')
    filename = "soil_building_copy.pdf"
    texfilename = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/soil12.tex'))
    texfilename_copy = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/soil_building_copy.tex'))
    report_get_id = Soil_building.objects.values('id'). \
    get(Session_id=data_session['Session'], Voucher = data_session['Voucher'])  	 
    report_content = '' 
    count = 1
    for des in  Soil_building_des.objects.filter(soil_building_report_id_id \
     = report_get_id['id']):
        report_content += str(count) + "&" + des.Dt + "&" + des.Ob_Pr \
         + "&" + des.Corr_F + "&" + des.Ob_N_V + "&" + des.Corr_N_V + "\\" \
         + "\\" + "\hline"
        count +=1        
    f = open(texfilename,'r+')
    data = f.read()
    f.close()
    fw = open(texfilename_copy,'w+')
    fw.write(data)
    fw.close()
    texfile = os.open(texfilename_copy,os.O_RDWR)
    os.write(texfile, render_to_string(texfilename_copy,{'title': \
        data_session['Site_Name'].replace('&','\&'),
	    'dateoftest': data_session['Date_of_Testing'].replace('&','\&'),
		'strtype': data_session['Type_of_str'].replace('&','\&'),
		'lati': data_session['Latitude_N'].replace('&','\&'),
		'logitude': data_session['Longitude_E'],
		'p1': data_session['Presence_1'],
		'p2': data_session['Presence_2'],
        's1':data_session['Submitted_1'],    
		's2': data_session['Submitted_2'],
		's3': data_session['Submitted_3'],
        'bore':data_session['Bore_Hole'],
		'sitename': data_session['Site_Name'],
        'watertable': data_session['Water_Table'],    
		'walldt': data_session['Wall_Dt'],
		'wallb': data_session['Wall_B'],
		'coldf': data_session['Col_Df'],
        'coll': data_session['Col_L'],
        'colb':data_session['Col_B'],
        'gamawall':data_session['Gama_wall'],
        'wallc':data_session['Wall_C'],
        'wallphey':data_session['Wall_Phay'],
        'wallpheyfe':data_session['Wall_Phay_Fe'],
        'wallnc':data_session['Wall_Nc'],
        'wallnq':data_session['Wall_Nq'],
        'wallny':data_session['Wall_Ny'],
        'wallsc':data_session['Wall_Sc'],
        'wallsq':data_session['Wall_Sq'],
        'wallsy':data_session['Wall_Sy'],
        'walldc':data_session['Wall_dc'],
        'walldqdy':data_session['Wall_dq_dy'],
        'wallw':data_session['Wall_w'],
        'wallpeq':data_session['Wall_peq'],
        'walltotal':data_session['Wall_Total'],
        'wallt2':data_session['Wall_T_2'],
        'colsc' :data_session['Col_Sc'],
        'colsq':data_session['Col_Sq'],                     
        'colsy':data_session['Col_Sy'],
        'coldc':data_session['Col_dc'],
        'coldqdy':data_session['Col_dq_dy'],
        'colpeq':data_session['Col_peq'],
        'coltotal':data_session['Col_Total'],
        'colt2':data_session['Col_T_2'],
        'wallnv':data_session['Wall_N_V'],
        'walls':data_session['Wall_S'],
        'wallvalue':data_session['Wall_Value'],
        'wallnetv':data_session['Wall_Net_V'],
        'wallgv':data_session['Wall_G_V'],
        'colnv':data_session['Col_N_V'],
        'colvalue':data_session['Col_Value'],
        'colnetv':data_session['Col_Net_V'],
        'colgv':data_session['Col_G_V'],
        'table':report_content,
		}))
    os.close(texfile)
    call(['sh',os.path.abspath(os.path.join(os.path.dirname(__file__), \
     '../..', 'templates/Test_Reports/shell.sh'))])   
    return render(request,"Test_Reports/soil.html",{"r":"/"+filename})

@login_required
def Soil_ohsr_report(request):
    data_session = request.session.get('data')
    filename = "set_copy.pdf"
    texfilename = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/set.tex'))
    texfilename_copy = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/set_copy.tex'))
    report_get_id = Soil_ohsr.objects.values('id').get(session_id= \
    data_session['session'], voucher = data_session['voucher'])    
    report_content = '' 
    count = 1
    for des in  Soil_ohsr_des.objects.filter(soil_ohsr_report_id_id =  \
        report_get_id['id']):
        report_content += str(count) + "&" + des.dt + "&" + des.ob_pr  \
        + "&" + des.corr_f + "&" + des.ob_n_v + "&" + des.corr_n_v + "\\" \
        + "\\" + "\hline"
        count +=1        
    f = open(texfilename,'r+')
    data = f.read()
    f.close()
    fw = open(texfilename_copy,'w+')
    fw.write(data)
    fw.close()
    texfile = os.open(texfilename_copy,os.O_RDWR)
    os.write(texfile, render_to_string(texfilename_copy, \
        {'title': data_session['site_name'].replace('&','\&'),
        'dateoftest': data_session['date_of_testing'].replace('&','\&'),
        'strtype': data_session['type_of_str'].replace('&','\&'),
        'lati': data_session['latitude_n'].replace('&','\&'),
        'logitude': data_session['longitude_e'],
        'p1': data_session['presence_1'],
        'p2': data_session['presence_2'],
        's1':data_session['submitted_1'],    
        's2': data_session['submitted_2'],
        's3': data_session['submitted_3'],
        'sitename': data_session['site_name'],
        'watertable': data_session['water_table'],    
        'depth': data_session['depth'],
        'diameter_B': data_session['diameter_b'],
        'gama_g': data_session['gama_g'],
        'C': data_session['c'],
        'phay':data_session['phay'],
        'phayfe':data_session['phayfe'],
        'nc':data_session['nc'],
        'nq':data_session['nq'],
        'ny':data_session['ny'],
        'dc':data_session['dc'],
        'dqdy':data_session['dqdy'],
        'water':data_session['water'],
        'pulse':data_session['pluse'],
        'eqtotal':data_session['eqtotal'],
        'totaldy':data_session['totaldby'],
        'nvalue':data_session['nvalue'],
        's':data_session['s'],
        'value':data_session['value'],
        'netvalue':data_session['netvalue'],
        'table':report_content,
        }))
    os.close(texfile)
    call(['sh',os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/shell.sh'))])   
    return render(request,"Test_Reports/soil.html",{"r":"/"+filename})

@login_required
def Soil_bridge_report(request):
    data_session = request.session.get('data')
    filename = "bridge_copy.pdf"
    texfilename = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/bridge.tex'))
    texfilename_copy = os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/bridge_copy.tex'))
    report_get_id = Soil_bridge.objects.values('id').get(session_id= \
    data_session['session'], voucher = data_session['voucher'])    
    report_content = '' 
    product_content = []
    product_material = []
    count = 1
    for product in Soil_bridge_des.objects.filter(soil_bridge_report_id_id =\
    report_get_id['id']):
        product_content.append(product.p_product)
        product_material.append(product.p_matretain)
    
    for des in  Soil_bridge_des.objects.filter(soil_bridge_report_id_id =\
    report_get_id['id']):
        report_content += str(count) + "&" + des.dt + "&" + des.ob_pr +\
         "&" + des.corr_f + "&" + des.ob_n_v + "&" + des.corr_n_v + "\\"\
         + "\\" + "\hline"
        count +=1        
    f = open(texfilename,'r+')
    data = f.read()
    f.close()
    fw = open(texfilename_copy,'w+')
    fw.write(data)
    fw.close()
    texfile = os.open(texfilename_copy,os.O_RDWR)
    os.write(texfile, render_to_string(texfilename_copy,{'title':  \
        data_session['site_name'].replace('&','\&'),
        'dateoftest': data_session['date_of_testing'].replace('&','\&'),
        'strtype': data_session['type_of_str'].replace('&','\&'),
        'lati': data_session['latitude_n'].replace('&','\&'),
        'logitude': data_session['longitude_e'],
        'p1': data_session['presence_1'],
        'p2': data_session['presence_2'],
        's1':data_session['submitted_1'],    
        's2': data_session['submitted_2'],
        's3': data_session['submitted_3'],
        'bore': data_session['water_table'],                                    
        'sitename': data_session['site_name'],
        'watertable': data_session['water_table'],   
        'siltf': data_session['silt_f'],
        'canal': data_session['canal_drain'],
        'openwall': data_session['open_wall'],
        'openwall2': data_session['open_wall_2'],
        'opendrain': data_session['open_drain'],
        'bedp': data_session['bed_particle'],
        'siltfactor': data_session['silt_factor'],
        'silt1': data_session['silt_1'],
        'dischargeq': data_session['discharge_q'],
        'qv': data_session['q_v'],                                                                                                            
        'bwidth': data_session['bed_width'],
        'bedv': data_session['bed_v'],
        'unitq': data_session['unit_q'],
        'p1':product_content[0],
        'pm1':product_material[0],
        'p2':product_content[1],
        'pm2':product_material[1],
        'p3':product_content[2],
        'pm3':product_material[2],
        'p4':product_content[3],
        'pm4':product_material[4],
        'p5':product_content[5],
        'pm5':product_material[5],
        'normalr': data_session['normal_r'],
        'max2r': data_session['max_2r'],
        'supply': data_session['supply_l'],
        'fsft': data_session['fs_ft'],
        'fsm': data_session['fs_m'],
        'bedlt': data_session['bedl_t'],
        'sayv': data_session['say_v'],
        'dfv': data_session['df_v'],
        'length': data_session['length_l'],
        'widthb': data_session['width_b'],
        'gamao': data_session['gama_o'],
        'oc': data_session['oc'],
        'ophay':data_session['o_phay'],
        'ophayfe':data_session['o_phay_fe'],
        'nc':data_session['o_nc'],
        'nq':data_session['o_nq'],
        'ny':data_session['o_ny'],
        'dc':data_session['o_dc'],
        'scsq':data_session['o_ScSq'],
        'sy':data_session['o_sy'],
        'dc':data_session['o_dc'],
        'dqdy':data_session['o_dqdy'],
        'o_w':data_session['o_w'],
        'o_peg':data_session['o_peg'],
        'o_total':data_session['o_total'],
        'o_t_2':data_session['o_t_2'],
        'nv':data_session['n_v'],
        'sv':data_session['s_v'],
        'value':data_session['value_av'],
        'net':data_session['net_v'],
        'gross':data_session['gross_v'],
        'table':report_content,
        }))
    os.close(texfile)
    call(['sh',os.path.abspath(os.path.join(os.path.dirname(__file__), \
    '../..', 'templates/Test_Reports/shell.sh'))])   
    return render(request,"Test_Reports/soil.html",{"r":"/"+filename,\
    "dd":product_material})