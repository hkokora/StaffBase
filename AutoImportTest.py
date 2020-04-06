from StaffBase import AutoImport

token = 'Enter Yours'
mappings = 'externalID,profile-field:firstName,profile-field:lastName,emails,,role,profile-field:avatar'
csv_location = 'path to the CSV file'
new_auto_import = AutoImport(token=token, csv=csv_location, mappings=mappings)
new_auto_import.upload_csv()
new_auto_import.update_csv_mappings(debug=True)
new_auto_import.final_update()


