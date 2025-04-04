def ingestion_tpapi(process, as_of_dt):
    try:
        lg.step_name = "getting date to run and CRDS code from DB"
        lg.start_step()

        crds_code_all = get_crds()
        print(len(crds_code_all))

        lg.end_step()

        lg.step_name = "Calling Change Notification Call"
        lg.start_step()

        print(as_of_dt)

        as_of_dt_str = as_of_dt.strftime('%d-%m-%Y')

        operator = "CHANGE NOTIFICATION"

        global tp_obj, status_obj

        tp_obj = TpapiInteract(process, as_of_dt)
        status_obj = StatusLog(process, as_of_dt.strftime('%d-%m-%Y'))

        status_obj.update_status(operator, 'Change notification call started - 1')

        batch_size = get_batchs(len(crds_code_all), 100)

        lg.rc = load_df_to_oracle(generate_data(crds_code_all, batch_size, process, operator, None),
                                  operator, process, ['crdsCode', 'kycId', 'ptyId'], as_of_dt)

        if lg.rc == 0:
            print(f"{operator} load successfully")
            status_obj.update_status(operator, 'Change notification load successfully - 2')
        else:
            print(f"{operator} does not load successfully")
            status_obj.update_status(operator, 'Change notification does not load successfully - 2')

        operator_config_dic, del_crds_rec = impacted_url(as_of_dt_str, process)

        lg.end_step()

        # Step 1: Run ENTITIES, ASSOCIATION, and ENTITIES_KYC together
        lg.step_name = "Executing ENTITIES, ASSOCIATION, and ENTITIES_KYC in one step"
        lg.start_step()

        for operator, field in operator_config_dic.items():
            if operator in ["ENTITIES", "ASSOCIATION", "ENTITIES_KYC"]:
                print(f"Running {operator}")
                lg.rc = endpoint_check(operator, field, process, del_crds_rec)

        lg.end_step()

        # Step 2: Run INDIVIDUAL separately
        lg.step_name = "Executing INDIVIDUAL in a separate step"
        lg.start_step()

        for operator, field in operator_config_dic.items():
            if operator == "INDIVIDUAL":
                print(f"Running {operator}")
                lg.rc = endpoint_check(operator, field, process, del_crds_rec)

        lg.end_step()

        return 0

    except ValueError:
        return 1
