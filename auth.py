from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, services
from ..dependencies import get_db, get_current_user, require_admin
from ..security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = services.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    new_user = services.create_user(
        db=db,
        email=user.email,
        password=user.password,
        role=user.role,
    )

    return {
        "message": "User created",
        "user_id": new_user.id,
        "role": new_user.role,
    }


@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, user.email)

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=schemas.UserResponse)
def read_me(current_user=Depends(get_current_user)):
    return current_user


@router.get("/admin-only")
def admin_only_route(current_user=Depends(require_admin)):
    return {
        "message": f"Welcome admin {current_user.email}"
    }