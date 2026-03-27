# Architecture Design: Auth Service

The Authentication System (Component C_Auth) handles all user identity verification.

It includes a Login Flow (Block B_Login) which is the main process for user authentication.

Inside this block, the Validate Email function (Function F_Validate_Email) checks if the email format is valid.

It uses the User Credentials data structure (Data D_User_Creds) which contains `username` and `password`.

The Login endpoint is public (Access A_Public).

A Successful Login (Event E_Login_Success) is emitted when a user successfully authenticates.
