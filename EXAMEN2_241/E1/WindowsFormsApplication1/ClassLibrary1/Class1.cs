using System;
using System.Data;
using System.Data.SqlClient;

namespace ClassLibrary1
{
    public class Class1
    {
        string connectionString = "Data Source=(local);Initial Catalog=academico;Integrated Security=True;";

        public Class1()
        {
        
        }

        


        public DataTable ExecuteSelectQuery(string tableName)
        {
            DataTable dataTable = new DataTable();

            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string query = "SELECT * FROM "+tableName;
                    using (SqlCommand command = new SqlCommand(query, connection))
                    {
                        using (SqlDataAdapter dataAdapter = new SqlDataAdapter(command))
                        {
                            dataAdapter.Fill(dataTable);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                // Manejo de excepciones
                throw new Exception("Error al ejecutar la consulta SQL", ex);
            }

            return dataTable;
        }
    }
}
